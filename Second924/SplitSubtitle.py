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
            
            if chinese_part:
                ch_file.write("".join(chinese_part) + "\n")
            if english_part:
                en_file.write("".join(english_part) + "\n")

# 调用函数
split_subtitle('The Shawshank Redemption-台词.txt', 'chinese_subtitle.txt', 'english_subtitle.txt')
