from enum import Enum

class State(Enum):
    StateInitial = 0
    StateIntSign = 1
    StateInteger = 2
    StatePoint = 3
    StatePointWithoutInt = 4
    StateFraction = 5
    StateExp = 6
    StateExpSign = 7
    StateExpNumber = 8
    StateEnd = 9

class Input(Enum):
    Number = 0
    Exp = 1
    Point = 2
    Sign = 3
    Space = 4
    Illegal = 5

StateTransitionGraph = {
    State.StateInitial: {
        Input.Space: State.StateInitial,
        Input.Number: State.StateInteger,
        Input.Point: State.StatePointWithoutInt,
        Input.Sign: State.StateIntSign,
    },
    State.StateIntSign: {
        Input.Number: State.StateInteger,
        Input.Point: State.StatePointWithoutInt,
    },
    State.StateInteger: {
        Input.Number: State.StateInteger,
        Input.Exp: State.StateExp,
        Input.Point: State.StatePoint,
        Input.Space: State.StateEnd,
    },
    State.StatePoint: {
        Input.Number: State.StateFraction,
        Input.Exp: State.StateExp,
        Input.Space: State.StateEnd,
    },
    State.StatePointWithoutInt: {
        Input.Number: State.StateFraction,
    },
    State.StateFraction: {
        Input.Number: State.StateFraction,
        Input.Exp: State.StateExp,
        Input.Space: State.StateEnd,
    },
    State.StateExp: {
        Input.Number: State.StateExpNumber,
        Input.Sign: State.StateExpSign,
    },
    State.StateExpSign: {
        Input.Number: State.StateExpNumber,
    },
    State.StateExpNumber: {
        Input.Number: State.StateExpNumber,
        Input.Space: State.StateEnd,
    },
    State.StateEnd: {
        Input.Space: State.StateEnd,
    },
}

class Solution:
    def isNumber(self, s: str) -> bool:
        def reflect(ch: str) -> Input:
            if ch.isdigit():
                return Input.Number
            elif ch.lower() == "e":
                return Input.Exp
            elif ch == ".":
                return Input.Point
            elif ch == "+" or ch == "-":
                return Input.Sign
            elif ch == " ":
                return Input.Space
            else:
                return Input.Illegal
        
        transfer = {
            State.StateInitial: {
                Input.Space: State.StateInitial,
                Input.Number: State.StateInteger,
                Input.Point: State.StatePointWithoutInt,
                Input.Sign: State.StateIntSign,
            },
            State.StateIntSign: {
                Input.Number: State.StateInteger,
                Input.Point: State.StatePointWithoutInt,
            },
            State.StateInteger: {
                Input.Number: State.StateInteger,
                Input.Exp: State.StateExp,
                Input.Point: State.StatePoint,
                Input.Space: State.StateEnd,
            },
            State.StatePoint: {
                Input.Number: State.StateFraction,
                Input.Exp: State.StateExp,
                Input.Space: State.StateEnd,
            },
            State.StatePointWithoutInt: {
                Input.Number: State.StateFraction,
            },
            State.StateFraction: {
                Input.Number: State.StateFraction,
                Input.Exp: State.StateExp,
                Input.Space: State.StateEnd,
            },
            State.StateExp: {
                Input.Number: State.StateExpNumber,
                Input.Sign: State.StateExpSign,
            },
            State.StateExpSign: {
                Input.Number: State.StateExpNumber,
            },
            State.StateExpNumber: {
                Input.Number: State.StateExpNumber,
                Input.Space: State.StateEnd,
            },
            State.StateEnd: {
                Input.Space: State.StateEnd,
            },
        }

        state = State.StateInitial
        for ch in s:
            input_type = reflect(ch)
            if input_type not in transfer[state]:
                return False
            state = transfer[state][input_type]
        
        return state in {
            State.StateInteger,
            State.StatePoint,
            State.StateFraction,
            State.StateExpNumber,
            State.StateEnd
        }