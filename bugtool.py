import json
import time
import requests

def bugtool():
    """获取bug信息 如状态 优先级等"""
    header = {
        "Accept":"*/*",
        "Connection":"keep-alive",
        "content-type":"application/json"
    }
    cookie = {"ajs_anonymous_id":"%22772a5426-d38d-40f4-91c7-ceedc0d30a3f%22","atlassian.xsrf.token":"725e5e66-f148-4f2e-a701-9a168378c0b7_cd0ba33e1b1cd5cb67bfc5665465f254f4037271_lin","jira.navigation.expandableMenuStates.classic-issues-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","jira.navigation.expandableMenuStates.classic-apps-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","JSESSIONID":"949AC3427B8A0790B91607BCB2E27F14","cloud.session.token":"eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI2Mjk3MDdlYjU2M2QzODAwNjhiMWQ3NzMiLCJlbWFpbERvbWFpbiI6InJjdC5haSIsImltcGVyc29uYXRpb24iOltdLCJjcmVhdGVkIjoxNjU0MDY1NDU4LCJyZWZyZXNoVGltZW91dCI6MTY1OTA2MjM3OSwidmVyaWZpZWQiOnRydWUsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6IjhlZTU3N2VjLWM1N2ItNGU0Yy1hZDc4LTYwZjM4YTYxY2MzZSIsInN0ZXBVcHMiOltdLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE2NTkwNjE3NzksImV4cCI6MTY2MTY1Mzc3OSwiaWF0IjoxNjU5MDYxNzc5LCJlbWFpbCI6IndhbmdsaWppZUByY3QuYWkiLCJqdGkiOiI4ZWU1NzdlYy1jNTdiLTRlNGMtYWQ3OC02MGYzOGE2MWNjM2UifQ.ndVFC8fH0OKdTivKUSMEg9Udkom6vueZ1dJq2WHjQechXkio_YjLE-KCP8R9f5HIT1BvRIQ5IXodm-DpfUPtJKrsrNxGmaPq8SrmAaez8S1WgFPvA1FKfGwBrOJZI2DUKdeSF9_S6Lb0ktYmOvtbnf7egp-hux6sLtEmCHaDzQG8X7Z2ImGrshqQPlU9iZBw9e-eK1xJi5U6yyitdFFFetj1mCE6TZAqTcUBEy5TRGTKJFZlbzo0eNRWFhglGfdl0MNY8wEbuTwDq2XYx9-J8tILLZnHpc34bh1hIDhPmS5YYMF1NJc3JBrdPLnPPKtFnS1sx9Vs7yFQSSz2Zx7xWg"}
    query = """query IssueListQuery($jql: String, $first: Int!, $last: Int, $filterId: Int, $amountOfIds: Int, $isMaxResultsLimitEnabled: Boolean!) {\n  issueIds: issues(first: $amountOfIds, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      issueId\n      __typename\n    }\n    __typename\n  }\n  issues(first: $first, last: $last, jql: $jql, filterId: $filterId, isMaxResultsLimitEnabled: $isMaxResultsLimitEnabled) {\n    nodes {\n      ...GetIssueDetails\n      __typename\n    }\n    ...GetTotalCountFragment\n    jql\n    __typename\n  }\n}\n\nfragment GetIssueDetails on Issue {\n  ...GetIdFragment\n  ...GetIssueIdFragment\n  ...GetIssueKeyFragment\n  ...GetAssigneeFragment\n  ...GetIssueTypeFragment\n  ...GetSummaryFragment\n  ...GetStatusFragment\n  ...GetReporterFragment\n  ...GetPriorityFragment\n  ...GetCreatedFragment\n  ...GetResolutionFragment\n  ...GetUpdatedFragment\n  ...GetDueDateFragment\n  __typename\n}\n\nfragment GetIdFragment on Issue {\n  __typename\n  id\n}\n\nfragment GetIssueIdFragment on Issue {\n  issueId\n  __typename\n}\n\nfragment GetIssueKeyFragment on Issue {\n  issuekey {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetAssigneeFragment on Issue {\n  assignee {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetIssueTypeFragment on Issue {\n  issuetype {\n    iconUrl\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetSummaryFragment on Issue {\n  summary {\n    textValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetStatusFragment on Issue {\n  status {\n    name\n    statusId\n    statusCategoryId\n    __typename\n  }\n  __typename\n}\n\nfragment GetReporterFragment on Issue {\n  reporter {\n    userValue {\n      accountId\n      avatarUrl\n      displayName\n      emailAddress\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GetPriorityFragment on Issue {\n  priority {\n    name\n    iconUrl\n    __typename\n  }\n  __typename\n}\n\nfragment GetCreatedFragment on Issue {\n  created {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetResolutionFragment on Issue {\n  resolution {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment GetUpdatedFragment on Issue {\n  updated {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetDueDateFragment on Issue {\n  duedate {\n    stringValue\n    __typename\n  }\n  __typename\n}\n\nfragment GetTotalCountFragment on GQLIssueConnection {\n  totalCount\n  __typename\n}\n"""
    variables = {"first": 50, "last": 50, "jql": "project = \"DX\" AND type = Bug AND fixVersion = \"Marketplace 3.1.0\" ORDER BY created DESC", "amountOfIds": 1000, "isMaxResultsLimitEnabled": True}
    url = 'https://rct-ai.atlassian.net/rest/gira/1/?operation=IssueListQuery'
    resp = requests.post(url=url, json={"operationName":"IssueListQuery","query": query,"variables":variables}, headers=header, cookies=cookie)
    print(resp.json())
    i = 0
    all = len(resp.json()['data']['issueIds']['nodes'])
    upUnFix = []
    P0UnFix = []
    P1UnFix = []
    AllUnFix = []
    while i < len(resp.json()['data']['issueIds']['nodes']):
        priority = resp.json()['data']['issues']['nodes'][i]['priority']['name']
        status = resp.json()['data']['issues']['nodes'][i]['status']['name']
        name = [str(resp.json()['data']['issues']['nodes'][i]['summary']['textValue'])]
        if priority == '阻止程序' and status == '打开' or priority == '阻止程序' and status == 'In Dev':
            upUnFix += name
        if priority == 'P0-重要紧急' and status == '打开' or priority == 'P0-重要紧急' and status == 'In Dev':
            P0UnFix += name
        if priority == 'P1-重要不紧急' and status == '打开' or priority == 'P1-重要不紧急' and status == 'In Dev':
            P1UnFix += name
        if status == '打开' or status == 'In Dev':
            AllUnFix += name
        i += 1
    print(upUnFix)
    print(P0UnFix)
    print(P1UnFix)
    print(AllUnFix)
    print(all)

    """修改格式推送至飞书"""
    upUnFixNum = len(upUnFix)
    P0UnFixNum = len(P0UnFix)
    P1UnFixNum = len(P1UnFix)
    AllUnFixNum = len(AllUnFix)

    upUnFixTitle = "\n*".join(upUnFix)
    P0UnFixTitle = "\n*".join(P0UnFix)
    P1UnFixTitle = "\n*".join(P1UnFix)
    AllUnFixTitle = "\n*".join(AllUnFix)

    today = time.strftime("%Y-%m-%d",time.localtime())
    p = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "tag": "div",
                "text": {
                        "content": "📒 **Marketplace 3.0**",
                        "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Above Unfixed Bugs  **{upUnFixNum}**\n*{upUnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Unfixed Bugs  **{P0UnFixNum}**\n*{P0UnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P1 Unfixed Bugs  **{P1UnFixNum}**\n*{P1UnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of All Unfixed Bugs  **{AllUnFixNum}**\n*{AllUnFixTitle}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Total Number Of Bugs  **{all}**",
                    "tag": "lark_md"
                }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": "🔍 CLICK HERE FOR DETAILS",
                                    "tag": "lark_md"
                            },
                            "url": "https://rct-ai.atlassian.net/jira/software/c/projects/DX/boards/43",
                            "type": "default",
                            "value": {}
                    }],
                    "tag": "action"
            }],
            "header": {
                    "title": {
                            "content": f"🔔  {today} BUG INFO",
                            "tag": "plain_text"
                    }
            }
        }
    }
    send = requests.post('https://open.feishu.cn/open-apis/bot/v2/hook/0da6a938-d932-4e91-86a0-86a3d43ecf11',json.dumps(p))
    print(send.status_code,send.json())
    return send

if __name__ == '__main__':
    bugtool()
