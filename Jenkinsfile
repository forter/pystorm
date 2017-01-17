// vim: filetype=groovy
node('master') {
    def base = load '/var/jenkins_home/workspace/Infra/build-scripts/build/Jenkinsfile'
    stages = base.get_pypi_stages()
    base.build([], 'repo', stages)
}