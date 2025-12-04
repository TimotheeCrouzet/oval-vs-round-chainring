import numpy as np
from ovalchainring.pedalling_model import (
    simulate_round,
    simulate_oval,
    compute_mean_torque,
    compute_dead_zone_duration,
)
from .chainrings_catalog import ChainringConfig


def compare_to_round(
    chainring: ChainringConfig,
    n: int = 360,
    threshold: float = 4.0,
    cadence_rpm: float = 90.0,
):
    """
    Simulate the selected chainring and compare it to a round reference chainring
    with the same mean radius.
    """
    # Round reference
    angle_round, torque_round, radius_round = simulate_round(
        R=chainring.R,
        n=n,
    )

    # Selected chainring
    if chainring.ovality == 0.0:
        angle_oval, torque_oval, radius_oval = (
            angle_round,
            torque_round.copy(),
            radius_round,
        )
    else:
        angle_oval, torque_oval, radius_oval = simulate_oval(
            R=chainring.R,
            ovality=chainring.ovality,
            timing=chainring.timing_rad,
            n=n,
        )

    # Mean torques and relative gain
    mean_torque_round = compute_mean_torque(torque_round)
    mean_torque_oval = compute_mean_torque(torque_oval)
    gain = (
        (mean_torque_oval - mean_torque_round) / mean_torque_round * 100.0
        if mean_torque_round != 0
        else 0.0
    )

    # Dead-zone durations (torque < threshold)
    dead_r, tot_r, pct_r = compute_dead_zone_duration(
        angle_round, torque_round, threshold, cadence_rpm
    )
    dead_o, tot_o, pct_o = compute_dead_zone_duration(
        angle_oval, torque_oval, threshold, cadence_rpm
    )

    return {
        "angle_deg": np.rad2deg(angle_round),
        "torque_round": torque_round,
        "torque_oval": torque_oval,
        "radius_round": radius_round,
        "radius_oval": radius_oval,
        "mean_torque_round": mean_torque_round,
        "mean_torque_oval": mean_torque_oval,
        "gain_percent": gain,
        "deadzone_round": {
            "dead_time": dead_r,
            "total_time": tot_r,
            "percent": pct_r,
        },
        "deadzone_oval": {
            "dead_time": dead_o,
            "total_time": tot_o,
            "percent": pct_o,
        },
    }
