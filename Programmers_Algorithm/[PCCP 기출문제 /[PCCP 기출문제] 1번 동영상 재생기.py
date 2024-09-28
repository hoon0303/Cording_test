def func(len):

    idx = len.find(":")
    s1 = len[0:idx]
    s2 = len[idx+1:]
    return int(s1)*60+int(s2)
    
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = func(video_len)
    pos = func(pos)
    op_start = func(op_start)
    op_end = func(op_end)
    
    if pos < 0:
        pos = 0
    if pos >= op_start and pos <= op_end:
        pos = op_end
    if pos > video_len:
        pos = video_len
    for command in commands:
        if command == "next":
            pos += 10
        elif command == "prev":
            pos -= 10
        if pos < 0:
            pos = 0
        if pos >= op_start and pos <= op_end:
            pos = op_end
        if pos > video_len:
            pos = video_len
    x = str(pos // 60)
    y = str(pos % 60)
    if int(x) // 10 == 0:
        x = '0'+x
    if int(y) // 10 == 0:
        y = '0'+y
    answer = x+':'+y
    return answer
