'''
level=hard
topic: DP, bit masking
logic:
Since dealing with strings, we map the given strings to some bit so that list of strings will be reduced to numbers
We maintain a dic to track min team size.
We will travel in person's skill list and on the go will update min team 
'''
class Solution:
    def __call__(self,req_skills: list[str], people: list[list[str]]) -> list[int]:
        return self.smallestSufficientTeam(req_skills, people)
    
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        # mapping req skills
        req_skill_map={skill:i for i, skill in enumerate(req_skills)}
        n=len(req_skills)

        min_team = {0:[]}
        for i, person in enumerate(people):
            # person's skill mapping
            person_skill_mask=0 
            for skill in person:
                person_skill_mask|=(1<<req_skill_map[skill]) 
            # checking in with skill set calculated so far
            for skill_set, team in list(min_team.items()):# here we are doing list on items because, on run time, size of dict will change.
                # creating what will be the new skill set
                new_skill_set =skill_set|person_skill_mask 
                # if skill set is already present or if new skill set team size is bigger
                if new_skill_set not in min_team or len(min_team[new_skill_set])>len(team)+1:
                    min_team[new_skill_set]=team+[i]

        return min_team[(1<<n) -1]
    
req_skill_list=[
    ["java","nodejs","reactjs"],
    ["algorithms","math","java","reactjs","csharp","aws"]
]

people_list_of_list=[
    [["java"],["nodejs"],["nodejs","reactjs"]],
    [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
]

def driver():
    for i in range(2):
        solver=Solution()
        print(solver(req_skill_list[i], people_list_of_list[i]))
        
if __name__=='__main__':
    driver()

            