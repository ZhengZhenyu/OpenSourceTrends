from github import Github
import pandas as pd

git_hub = Github()

project_list = ['Apache/Hadoop', 'Apache/Hive', 'Apache/Spark', 'Apache/Hbase',
        'Apache/Flink']
github_df = pd.DataFrame(columns=project_list)

for project in project_list:
    repo = git_hub.get_repo(project)
    participation = repo.get_stats_participation()
    commit_count_last_month = sum(participation.all[48:])
    github_df

print(commit_count_last_month)