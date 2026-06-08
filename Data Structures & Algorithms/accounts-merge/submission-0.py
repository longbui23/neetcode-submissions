class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = [i for i in range(n)]
        email_to_id = {}

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parents[ry] = rx

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i
        
        groups = defaultdict(list)
        for email, i in email_to_id.items():
            root = find(i)
            groups[root].append(email)

        res = []
        for i, emails in groups.items():
            res.append([accounts[i][0]] + sorted(emails))
        
        return res

