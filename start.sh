#!/usr/bin/env bash
data="${PWD}/ignore/jenkins_home"
rm -rf "${data}"
mkdir -p "${data}"
cmd=(
    container run
    -it
    --rm
    -v "${data}:/var/jenkins_home"
    -p 8080:8080
    "${@}"
    jenkins/jenkins
)
echo "${cmd[@]}"
exec "${cmd[@]}"
