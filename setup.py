import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name="Treasure Hunt",
                options={"build_exe": {"packages":["pygame"],
                                       "include_files":["sprites", "audio"]}},
                executables = executables)
