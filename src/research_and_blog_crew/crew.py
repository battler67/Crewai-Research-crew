from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ResearchAndBlogCrew():    

    agents:list[BaseAgent]
    tasks:list[BaseAgent]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config = self.agents_config["report_generator"]
        )
    
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config =  self.agents_config["blog_writer"]
        )
    
    @task
    def report_task(self) ->Task:
        return Task(
            config=self.tasks_config["report_task"]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config = self.tasks_config["blog_writing_task"],
            output_file = "blogs/blog.md"
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )
