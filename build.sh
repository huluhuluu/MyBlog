#!/usr/bin/env bash
set -euo pipefail

HUGO_VERSION="${HUGO_VERSION:-0.161.1}"
HUGO_DIR=".vercel-hugo"
HUGO_ARCHIVE="hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_ARCHIVE}"

mkdir -p "${HUGO_DIR}"

if [ ! -x "${HUGO_DIR}/hugo" ] || ! "${HUGO_DIR}/hugo" version | grep -q "v${HUGO_VERSION}"; then
    curl -fsSL "${HUGO_URL}" -o "/tmp/${HUGO_ARCHIVE}"
    tar -xzf "/tmp/${HUGO_ARCHIVE}" -C "${HUGO_DIR}" hugo
fi

git submodule update --init --recursive

"${HUGO_DIR}/hugo" version
"${HUGO_DIR}/hugo" --gc
