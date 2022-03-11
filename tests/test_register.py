import roster


def test_default() -> None:
    register: roster.Register = roster.Register()

    register("Ben", age=10)("ben")
    register("Sam", age=25)("sam")

    assert register == {
        "ben": roster.Context("Ben", age=10),
        "sam": roster.Context("Sam", age=25),
    }


def test_hooked() -> None:
    register: roster.Register = roster.Register(hook=dict)

    register(name="Ben", age=10)("ben")
    register(name="Sam", age=25)("sam")

    assert register == {
        "ben": {
            "name": "Ben",
            "age": 10,
        },
        "sam": {
            "name": "Sam",
            "age": 25,
        },
    }
