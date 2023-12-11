Собирался протестировать методику фазз-тестирования, почитал статьи на Хабре, вроде в голове сложилось что и как сделать, но на стадии реализации возникли проблемы.

Не удаётся поставить библиотеку через pip3 install atheris:

```
  Building wheel for atheris (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for atheris (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [27 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win-amd64-cpython-310
      copying atheris_no_libfuzzer.py -> build\lib.win-amd64-cpython-310
      creating build\lib.win-amd64-cpython-310\atheris
      copying src\coverage_g3test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\coverage_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\coverage_test_helper.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\custom_crossover_fuzz_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\custom_mutator_and_crossover_fuzz_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\custom_mutator_fuzz_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\function_hooks.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\fuzzed_data_provider_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\fuzz_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\fuzz_test_lib.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\hook-atheris.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\import_hook.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\instrument_bytecode.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\pyinstaller_coverage_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\regex_match_generation_test.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\utils.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\version_dependent.py -> build\lib.win-amd64-cpython-310\atheris
      copying src\__init__.py -> build\lib.win-amd64-cpython-310\atheris
      running build_ext
      error: [WinError 193] %1 не является приложением Win32
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for atheris
Failed to build atheris
ERROR: Could not build wheels for atheris, which is required to install pyproject.toml-based projects
PS C:\Users\n.sergushenkov\drafts> 
```

Отдельно выполнил pip install pyproject-toml - установка прошла нормально. Повторная попытка установить atheris выдаёт все те же ошибки. Попытка установить из сорцев - тоже падает, на cmake -DLLVM_ENABLE_PROJECTS='clang;compiler-rt' -G "Unix Makefiles" ../llvm
Возможно причина в корпоративных политиках безопасности на ноутбуке, но другого железа сейчас нет.
Убив полдня на эксперименты - решил отказаться от этой идеи.

По большому счету - у меня просто нет проектов, где это можно было бы всерьёз применить. По работе последние пару лет только SQL, личные проекты - учебные задачи и головоломки типа Advent of Code, там вероятность что будет что-то нестандартное практически равна нулю. 
Вот если бы писал какие то сетевые приложения - тогда да, инструмент был бы полезен.

В общем - решил отложить знакомство с фазингом на будущее.