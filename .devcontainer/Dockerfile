ARG QT_VERSION=6.8.3
FROM carlonluca/qt-dev:${QT_VERSION}

RUN (groupadd --gid 1000 vscode 2>/dev/null || true) \
	&& (useradd -s /bin/bash --uid 1000 --gid 1000 -m vscode 2>/dev/null || usermod -l vscode -d /home/vscode -m $(getent passwd 1000 | cut -d: -f1) || true)

USER vscode

ENV UV_CONSTRAINT=/home/vscode/.config/qt-constraints.txt
ENV UV_PROJECT_ENVIRONMENT=/home/vscode/.venv

RUN wget -qO- https://astral.sh/uv/install.sh | sh \
	&& export PATH="/home/vscode/.local/bin:$PATH"

# Generate PyQt6 version constraints based on Qt version
RUN QT_MINOR=$(echo ${QT_VERSION} | cut -d. -f1-2) \
	&& mkdir -p $(dirname ${UV_CONSTRAINT}) \
	&& echo "PyQt6~=${QT_MINOR}.0" > ${UV_CONSTRAINT}
