PROGRAM Parallel_Hello_World
USE OMP_LIB

INTEGER :: partial_Sum, total_Sum

!$OMP PARALLEL PRIVATE(partial_Sum) SHARED(total_Sum)
    partial_Sum = 0;
    total_Sum = 0;

    !$OMP DO
    DO i=1,100000000
        partial_Sum = partial_Sum + i
        
        
        partial_Sum = partial_Sum + atan(0.)
        partial_Sum = partial_Sum + atan(0.)
        partial_Sum = partial_Sum - atan(0.)
        partial_Sum = partial_Sum - atan(0.)
        
        
    END DO
    !$OMP END DO

    !$OMP CRITICAL
        total_Sum = total_Sum + partial_Sum
    !$OMP END CRITICAL

!$OMP END PARALLEL
PRINT *, "Total Sum: ", total_Sum

END