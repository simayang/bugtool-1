import json
import time
import requests

def bugtool():
    """获取所有bug的isuue key"""
    header = {
        "Accept":"*/*",
        "Connection":"keep-alive",
        "content-type":"application/json"
    }
    cookie = {"ajs_anonymous_id":"%22772a5426-d38d-40f4-91c7-ceedc0d30a3f%22","atlassian.xsrf.token":"725e5e66-f148-4f2e-a701-9a168378c0b7_59a5792dc995eab7552428c0b311fbd89db85622_lin","jira.navigation.expandableMenuStates.classic-issues-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","jira.navigation.expandableMenuStates.classic-apps-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","JSESSIONID":"1FEE672FBE81D9B263B80015D9998C0","cloud.session.token":"eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI2Mjk3MDdlYjU2M2QzODAwNjhiMWQ3NzMiLCJlbWFpbERvbWFpbiI6InJjdC5haSIsImltcGVyc29uYXRpb24iOltdLCJjcmVhdGVkIjoxNjU0MDY1NDU4LCJyZWZyZXNoVGltZW91dCI6MTY1NjM4ODI3NywidmVyaWZpZWQiOnRydWUsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6IjhlZTU3N2VjLWM1N2ItNGU0Yy1hZDc4LTYwZjM4YTYxY2MzZSIsInN0ZXBVcHMiOltdLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE2NTYzODc2NzcsImV4cCI6MTY1ODk3OTY3NywiaWF0IjoxNjU2Mzg3Njc3LCJlbWFpbCI6IndhbmdsaWppZUByY3QuYWkiLCJqdGkiOiI4ZWU1NzdlYy1jNTdiLTRlNGMtYWQ3OC02MGYzOGE2MWNjM2UifQ.Vkm7Ea_muGHtWfFfTh-Oxq6oxTQeR6PANjb4VbWUW2a3-2mGmUl3NOlmAO6l7i_dQKM5slYvY4n1c8zFE8MPPkR5XqXjMGgyGMmKd8HVIa90hPMpXaUeUdlI-wUqc5rLYYA-UXLgP9ORFHNzLUBW6B5lMb4df0Y3VuGcgWkkiFv-QilDFI6zuOMV6TGVZobfbILJdyqJoWQyLvH2B5sji4-ddz3g71Y5hUKU_FN-mULEo5Wq5yrTdS70VaFOvzxQ1f8vy_SWGVhgtKSj3-51aA4AG8BvBpgU1IyGm8u8_ioToBIKjGPdtnPP9VQhn4EmNEnpDqbVHDHOHK47BcU2rw"}
    url = 'https://rct-ai.atlassian.net/gateway/api/xpsearch-aggregator/quicksearch/v1'
    payload = {"query":"","cloudId":"54cc4c96-c35c-40fa-8ed3-81f8781efc95","limit": 50,"scopes":["jira.issue"],"filters":[],"searchSession":{"sessionId":"c1e5b4ac-f3b8-4475-bc43-8961a22ec1aa","referrerId":None},"experience":"jira.nav-v3","cloudIds":[]}
    resp = requests.post(url,data = json.dumps(payload),headers=header,cookies=cookie)
    result = resp.json()['scopes'][0]['results']
    print(resp.json()['scopes'][0]['results'])
    print(type(result),len(result))
    #print(resp.json()['scopes'][0]['results'][0]['attributes']['issueTypeId'],type(resp.json()['scopes'][0]['results'][0]['attributes']['issueTypeId']))
    #print(type(resp.json()['scopes'][0]['results'][0]['url']))
    i = 0
    bugs = []
    while i < len(result):
        if resp.json()['scopes'][0]['results'][i]['attributes']['issueTypeId'] == '10004' and resp.json()['scopes'][0]['results'][i]['attributes']['container']['id'] == '10024':
             bugs += [str(resp.json()['scopes'][0]['results'][i]['url'])[-5:]]
        i += 1
    print(bugs)

    """获取bug信息 如状态 优先级等"""

    url1 = 'https://rct-ai.atlassian.net/rest/graphql/1/'
    upUnFixNum = []
    P0UnFix = []
    P1UnFix = []
    AllUnFix = []
    j = 0
    while j < len(bugs):
        query = """query {\n        issue(issueIdOrKey: \""""+bugs[j]+"""\", latestVersion: true, screen: \"view\") {\n            id\n            viewScreenId \n            fields {\n                key\n                title\n                editable\n                required\n                autoCompleteUrl\n                allowedValues\n                content\n                renderedContent\n                schema {\n                    custom\n                    system\n                    configuration {\n        key\n        value\n    }\n    \n                    items\n                    type\n                    renderer\n                }\n                configuration\n            }\n            expandAssigneeInSubtasks\n            expandAssigneeInIssuelinks\n            expandTimeTrackingInSubtasks\n            systemFields {\n                descriptionAdf {\n                    value\n                }\n                environmentAdf {\n        value\n    }\n            }\n            customFields {\n                textareaAdf {\n                    key\n                    value\n                }\n            }            \n            tabs {\n        id\n        name\n        items {\n            id\n            type\n        }\n    }\n            \n    isHybridAgilityProject\n    \n            \n    agile {\n        epic {\n          key\n        },\n    }\n        }\n        \n        project(projectIdOrKey: \"NLP\") {\n            id\n            name\n            key\n            projectTypeKey\n            simplified\n            avatarUrls {\n                key\n                value\n            }\n            archived\n            deleted\n        }\n    }"""
        resp1 = requests.post(url=url1, json={"query": query}, headers=header, cookies=cookie)
        print(resp1.json())
        priority = resp1.json()['data']['issue']['fields'][18]['content']['id']
        status = resp1.json()['data']['issue']['fields'][28]['content']['name']
        name = [str(resp1.json()['data']['issue']['fields'][11]['content'])]
        #reqName = resp1.json()['data']['issue']['fields'][7]['content']['name']
        if priority == '1' and status == '打开' or priority == '1' and status == 'In Dev':
            upUnFixNum += name
        if priority == '2' and status == '打开' or priority == '2' and status == 'In Dev':
            P0UnFix += name
        if priority == '3' and status == '打开'or priority == '3' and status == 'In Dev':
            P1UnFix += name
        if status == '打开'or status == 'In Dev':
            AllUnFix += name
        j += 1
    print(upUnFixNum)
    print(P0UnFix)
    print(P1UnFix)
    print(AllUnFix)

    url2 = ' https://rct-ai.atlassian.net/rest/greenhopper/1.0/xboard/work/allData.json?rapidViewId=43&selectedProjectKey=DX&forceConsistency=false&_=1657274636276'
    resp2 = requests.get(url=url2,headers=header,cookies=cookie)
    print(resp2.json()['columnsData']['columns'],len(resp2.json()['columnsData']['columns']))
    t = 0
    Total = 0
    while t < len(resp2.json()['columnsData']['columns']):
        Total += resp2.json()['columnsData']['columns'][t]['statisticsFieldValue']
        t += 1
    print(Total)
    upUnFixNum = len(upUnFixNum)
    P0UnFixNum = len(P0UnFix)
    P1UnFixNum = len(P1UnFix)
    AllUnFixNum = len(AllUnFix)

    """修改格式推送至飞书"""
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
                        "content": "**📒 Project Name:Delysium Tech**",
                        "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Above Unfixed Bugs **{upUnFixNum}**",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P0 Unfixed Bugs **{P0UnFixNum}**",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of P1 Unfixed Bugs  **{P1UnFixNum}**",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Number Of All Unfixed Bugs **{AllUnFixNum}**",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"Total Number Of Bugs **{int(Total)}**",
                    "tag": "lark_md"
                }
            }, {
                    "actions": [{
                            "tag": "button",
                            "text": {
                                    "content": "🔍CLICK HERE FOR MORE DETAILS",
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
                            "content": f"🔔 {today} The Number Of Bugs From Jira",
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