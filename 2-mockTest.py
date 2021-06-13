def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if (answers[i] == num1[i % 5]):
            score[0] += 1
        if (answers[i] == num2[i % 8]):
            score[1] += 1
        if (answers[i] == num3[i % 10]):
            score[2] += 1

    print(score)

    if (score[0] >= score[1] and score[0] >= score[2]):
        answer.append(1)
    if (score[1] >= score[0] and score[1] >= score[2]):
        answer.append(2)
    if (score[2] >= score[1] and score[2] >= score[0]):
        answer.append(3)

    return answer

if __name__ == '__main__':
    answers = [1,2,3,4,5]
    print(solution(answers))