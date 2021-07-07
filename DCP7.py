# Medium

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


def countWaysHelper(codedMsg):
    msgLen = len(codedMsg)
    if msgLen == 1 or msgLen == 0:
        return 1

    count = 0
    if int(codedMsg[msgLen-2]) == 2 and int(codedMsg[msgLen-1]) < 7 or int(codedMsg[msgLen-2]) == 1:

        count += countWaysHelper(codedMsg[0:-2])

    count += countWaysHelper(codedMsg[0:-1])

    return count


def countWays(codedMsg):
    msgLen = len(codedMsg)
    if msgLen == 1:
        print(1)
        return

    print(countWaysHelper(codedMsg))


if __name__ == '__main__':
    countWays('161968816516')  # 16
