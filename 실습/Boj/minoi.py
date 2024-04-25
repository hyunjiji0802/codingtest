def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    temp_peg = 6-start_peg - end_peg
    #if num_disks == 0: return
    if num_disks == 1:
        move_disk(1, start_peg, end_peg)
        return
    print('hanoi(%d, %d, %d)함수 실행'%(num_disks-1, start_peg, temp_peg))
    hanoi(num_disks-1, start_peg, temp_peg)
    move_disk(num_disks, start_peg, end_peg)
    print('hanoi(%d, %d, %d)함수 실행'%(num_disks-1, temp_peg, end_peg))
    hanoi(num_disks - 1, temp_peg, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)

'''
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동
'''