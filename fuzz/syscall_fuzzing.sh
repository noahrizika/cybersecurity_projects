new_dir="fuzz_test"
mkdir $new_dir 
for syscall in {1..5}
do
	file_name="$new_dir/syscall-$syscall"
	echo <<- END
		BITS 64
		GLOBAL _start
		SECTION .text
		_start:
			mov rax, $syscall
			mov rdi, $($RANDOM % 200)
			mov rsi, $($RANDOM % 200)
			mov rdx, $($RANDOM % 200)
			syscall
			mov rax, 231
			mov rdi, 42
			syscall
	END
	< $file_name.asm

	nasm -f elf64 -o $file_name.bin $file_name.asm
	ld -o $file_name $file_name.bin

	echo "syscall code: $syscall" > $file_name-results.txt
	$file_name >> $file_name-results.txt
done

#analyze files and create a final report
report_path="$new_dir/report.txt"
echo "FUZZING REPORT" > $report_path 
echo "\nNumber of SegFaults: " >> $report_path
grep -r "SEGFAULT" $new_dir | wc -l >> $report_path
echo "\nSegFault Data: " >> $report_path 
grep -r "SEGFAULT" $new_dir >> $report_path
