""  # Temporary workaround until Poetry supports scripts
# https://github.com/sdispater/poetry/issues/241.
from subprocess import check_call
from pathlib import Path


module_id = "cog_ingester"
project_id = "cog-ingester"
project = "ccore-looknorth"


def format() -> None:
    check_call(["black", module_id, "tests/"])


def start() -> None:
    check_call(["python", "-m", f"{module_id}.api"])


def api() -> None:
    check_call(["python", "-m", f"{module_id}.api"])


def test() -> None:
    check_call(["pytest", "tests/"])


def freeze() -> None:
    with open("requirements.txt", "w") as file:
        check_call(["poetry", "export", "-f", "requirements.txt"], stdout=file)


def docker_build() -> None:
    check_call(["docker", "build", "-t", f"gcr.io/{project}/{project_id}:latest", "."])


def docker_run() -> None:
    check_call(
        [
            "docker",
            "run",
            "--rm",
            "-it",
            "-p",
            "8080:8080",
            "-t",
            f"gcr.io/{project}/{project_id}:latest",
        ]
    )


def docker() -> None:
    freeze()
    docker_build()
    docker_run()


def docker_build_run() -> None:
    docker_build()
    docker_run()


def docker_run_bash() -> None:
    check_call(
        [
            "docker",
            "run",
            "--rm",
            "-it",
            "-p",
            "8080:8080",
            "-t",
            f"gcr.io/{project}/{project_id}:latest",
            "/bin/bash",
        ]
    )


def docker_push() -> None:
    check_call(["docker", "push", f"gcr.io/{project}/{project_id}:latest"])


def docker_deploy() -> None:
    freeze()
    docker_build()
    docker_push()

    check_call(
        [
            "gcloud",
            "beta",
            "run",
            "deploy",
            project_id,
            "--image",
            f"gcr.io/{project}/{project_id}:latest",
            "--platform=managed",
            "--allow-unauthenticated",
            "--concurrency=1",
            "--memory=2Gi",
            "--timeout=15m",
            f"--project={project}",
        ]
    )


def docker_build_deploy() -> None:
    docker_build()
    docker_push()
    docker_deploy()


def deploy() -> None:
    docker_deploy()


def batch() -> None:
    check_call(
        [
            "python",
            "-m",
            f"{module_id}.batch"
        ]
    )
