DOCKER_NAME := forter-pystorm
DOCKER_REPO := 174522763890.dkr.ecr.us-east-1.amazonaws.com
GIT_HEAD_HASH := $(shell git --no-pager log -1 --pretty=format:%H)
ci-test: ##@CI CI tests
	docker run --rm -u 1666 -v ${PWD}/test-reports:/test-reports/:rw forter/${DOCKER_NAME} py.test --junitxml /test-reports/pytest.xml

build: ##@CI Build docker image
	@echo "on branch ${BRANCH_NAME}"
	docker build -t forter/${DOCKER_NAME} --label "git-commit=${GIT_HEAD_HASH}" .

dist:
	@echo "done"