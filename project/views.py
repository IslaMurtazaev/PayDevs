from django.shortcuts import render
from project.serializers import ProjectSerializer, ProjectListSerializer
from PayDevs.decorators import serialize_exception

class ProjectView(object):
	def __init__(self, get_project_interactor):
		self.get_project_interactor=get_project_interactor

	@serialize_exception
	def get(self, title):
		project = self.get_project_interactor.set_params(title=title).execute()
		body = ProjectSerializer.serializer(project)
		status = 200
		return body, status


class ProjectAllView(object):
	def __init__(self, get_project_interactor):
		self.get_project_interactor=get_project_interactor

	@serialize_exception
	def get(self, title):
		project = self.get_project_interactor.set_params(title=title).execute()
		body = ProjectLilstSerializer.serializer(projects
		status = 200
		return body, status