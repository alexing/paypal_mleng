"""
1. Efficient Teams
A coding competition is being organized on the HackerRank platform. All participants need to be grouped into teams where each team has exactly two candidates and the sums of their skills must be equal for all teams. The efficiency of a team is the product of the skills of its members, e.g. for a team with skills [2, 3], the efficiency of the team is 2 * 3 = 6.
Find the sum of the efficiencies of the teams. If there is no way to create teams that satisfy the conditions, return -1.

Notes
    All participants must be assigned to a team.
    The answer is always unique.

Example
The skills of the candidates are skill = [1, 2, 3, 2]. They can be paired as [[1, 3], [2, 2]]. The sum of skills for each team is the same, i.e., 4.
The efficiency is computed as:
    Efficiency of [1, 3] = 1 * 3 = 3
    Efficiency of [2, 2] = 2 * 2 = 4
Return the sum of efficiencies, 3 + 4 = 7.


Function Description
Complete the function getTotalEfficiency in the editor below.
getTotalEfficiency has the following parameter:
    int skill[n]: the skills of each candidate

Returns
    long_int: the sum of the efficiencies if it is possible to form the teams, or -1 otherwise

Constraints
    1 ≤ n ≤ 105
    1 ≤ skill[i] ≤ 105
    n is even.
    It is guaranteed that the answer is unique.
"""

from typing import List


def getTotalEfficiency(skills: List[int]) -> int:
    skills.sort()
    n = len(skills)

    total_efficiency = 0
    pair_sum = skills[0] + skills[-1]

    for i in range(n // 2):
        if skills[i] + skills[-1 - i] != pair_sum:
            return -1
        total_efficiency += skills[i] * skills[-1 - i]

    return total_efficiency


if __name__ == "__main__":
    assert getTotalEfficiency([1, 2, 3, 2]) == 7
