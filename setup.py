import cx_Freeze

executables = [cx_Freeze.Executable("simulacion.py",base=None,icon=None)]
build_exe_options = {
    "packages":["tabulate","memoria","cpu","memSec","so","planifCortoplazo","planifMedianoPlazo","planifLargoPlazo","proceso","particion","msvcrt"],
    "include_files":["proceso.py","so.py","files/procesos.txt","cpu.py"
        ,"memSec.py","planifCortoplazo.py","planifLargoPlazo.py","planifMedianoPlazo.py","particion.py","memoria.py"
    ]
}

cx_Freeze.setup(
    name= "simulacion prueba",
    version = "1.0",
    description = "Juego", 
    options = {"build_exe": build_exe_options}, 
    executables = executables
)