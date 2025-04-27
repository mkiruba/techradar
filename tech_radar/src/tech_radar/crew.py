from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TechRadar():
	"""TechRadar crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def backend_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['backend_expert'],
			verbose=True
		)

	@agent
	def frontend_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['frontend_expert'],
			verbose=True
		)

	@agent
	def testing_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['testing_expert'],
			verbose=True
		)

	@agent
	def coordinator(self) -> Agent:
		return Agent(
			config=self.agents_config['coordinator'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def backend_task(self) -> Task:
		return Task(
			config=self.tasks_config['backend_task'],
			output_file='src/tech_radar/files/backend_analysis.md'
		)

	@task
	def frontend_task(self) -> Task:
		return Task(
			config=self.tasks_config['frontend_task'],
			output_file='src/tech_radar/files/frontend_analysis.md'
		)

	@task
	def testing_task(self) -> Task:
		return Task(
			config=self.tasks_config['testing_task'],
			output_file='src/tech_radar/files/testing_analysis.md'
		)

	@task
	def coordinator_task(self) -> Task:
		return Task(
			config=self.tasks_config['coordinator_task'],
			output_file='src/tech_radar/files/coordinator_summary.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TechRadar crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
