#!/usr/bin/env bash

# ---------------------------------------------------------
abort() {
  if test -n "$1"; then
    echo >&2 -e "\n\nFAILED: $1\n\n"
  fi
  exit 1
}

trap 'abort' 0

set -e
set -o pipefail

# ---------------------------------------------------------

function contains() {
    local n=$#
    local value=${!n}
    for ((i=1; i < $#; i++)) {
        if [ "${!i}" == "${value}" ]; then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

assert_names() {
  dir_names=$(ls -d solutions/* | sed -e 's/solutions\///g')
  github_names=(
    "alex_moroz"
    "alexander_sidorov"
    "anastasiya_taranova"
    "andrey_lyah"
    "ekaterina_sushko"
    "eugene_ivashkevich"
    "katsiaryna_kutseika"
    "masha_gul"
    "roman_makarov"
    "ruslan_dolgolikov"
    "sergey_kasperovich"
    "yuriy_yakovlev"
    "yury_kashkur"
  )

  for n in ${dir_names}; do
    if [[ $n == "__init__.py" ]]; then
      continue;
    fi

    if [[ $(contains "${github_names[@]}" "$n") == "n" ]]; then
      echo "unknown Github name in solutions/: '$n'"
      return 1
    fi

    pkg_init_py="solutions/$n/__init__.py"
    if [[ ! -f $pkg_init_py ]]; then
      echo "File $pkg_init_py MUST be added"
      return 1
    fi
  done
}

# ---------------------------------------------------------

rm -rf solutions/__pycache__

# checks

assert_names || abort "MESS WITH USERS NAMES"

# ---------------------------------------------------------
trap : 0
# ---------------------------------------------------------
