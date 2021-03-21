# 3-ary: three operands. The first operand (the condition) is evaluated, and if it is true, the result of the entire expression is the value of the second operand, otherwise it is the value of the third operand

lockdown = True

bank_account = 150

status = "stay at home" if lockdown or bank_account < 100 else "have fun"
