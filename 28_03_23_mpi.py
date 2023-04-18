from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank() #num del procesos en los que sde está ejecutando
size = comm.Get_size() #total de procesos

print(f'{rank}/{size}')