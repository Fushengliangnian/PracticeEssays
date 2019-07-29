from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # @task
    # def sleep(self):
    #     self.client.get("/v3/test1")

    @task
    def sleep2(self):
        self.client.get("/")

    # @task
    # def sleep2(self):
    #     self.client.get("/v3/test3")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0  # ms
    max_wait = 1


# locust --host=http://localhost:8888    @task
