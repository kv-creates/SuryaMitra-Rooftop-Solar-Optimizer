from src.optimizer import optimize_joint
def test_joint_best():
    o = optimize_joint(19.07, 105, 40.0)
    assert o["best"]["daily_kwh"] > 0
    assert len(o["table"]) == 5
    assert o["best"]["azim_deg"] == 180
