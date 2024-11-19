def is_english(char):
    # 判断字符是否为英文字符
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def split_subtitle(input_file, chinese_file, english_file):
    with open(input_file, 'r', encoding='gbk') as infile, \
         open(chinese_file, 'w', encoding='utf-8') as ch_file, \
         open(english_file, 'w', encoding='utf-8') as en_file:
        
        for line in infile:
            chinese_part = []
            english_part = []
            for char in line:
                if is_english(char):
                    english_part.append(char)
                elif '\u4e00' <= char <= '\u9fff':  # 判断是否为中文字符
                    chinese_part.append(char)
                else:
                    # 在非英文字符处添加空格
                    if english_part and english_part[-1] != ' ':
                        english_part.append(' ')
            
            if chinese_part:
                ch_file.write("".join(chinese_part) + "\n")
            if english_part:
                # 去除末尾多余的空格
                en_file.write("".join(english_part).strip() + "\n")

# 调用函数
split_subtitle('The Shawshank Redemption-台词.txt', 'chinese_subtitle.txt', 'english_subtitle.txt')
