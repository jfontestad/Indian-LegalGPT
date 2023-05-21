import re
import json

class LawFileReader:
    def __init__(self, chapter_pattern=r"Chapter [0-9]+\b", entry_pattern=r"Article [0-9]+\b"):
        # Identifying chapter and entry
        self.chapter_pattern = chapter_pattern
        self.entry_pattern = entry_pattern

    def read_file(self, file_path):
        # Reading the file
        self.law = {}
        f = open(file_path, encoding='utf-8')
        content = f.read()
        content = content.replace("\n\n", "\n")
        content = content.replace("##", "")
        # print(content)
        chapter_match = re.search(self.chapter_pattern, content)
        while chapter_match is not None:
            c_start = chapter_match.start()
            c_end = chapter_match.end()
            key = content[c_start:c_end]
            content = content[c_end:]

            chapter_match = re.search(self.chapter_pattern, content)
            if chapter_match is not None:
                end = chapter_match.start()
                c_content = content[:end]
                self.law[key] = self.read_entries(c_content)
            # print(content[c_start:c_end])
            else:
                self.law[key] = self.read_entries(content)
        f.close()
        return self.law

    def read_entries(self, content):
        entries = {}
        entry_match = re.search(self.entry_pattern, content)
        while entry_match is not None:
            e_start = entry_match.start()
            e_end = entry_match.end()
            key = content[e_start:e_end]
            content = content[e_end+1:]

            entry_match = re.search(self.entry_pattern, content)
            if entry_match is not None:
                end = entry_match.start()
                e_content = content[:end]
                entries[key] = e_content
            else:
                entries[key] = content
        return entries

    def show(self):
        for key in self.law:
            print(key, '\n')
            for item in self.law[key]:
                print(item, ' ', self.law[key][item])


if __name__ == '__main__':
    file_path = "D:/11496/Documents/project/Laws-master/Economic Law/Price Law(1997-12-29).md"
    r = LawFileReader()
    dict = r.read_file(file_path)
    r.show()
    print(dict)
    with open('./a.json', 'w') as f:
        json.dump(dict, f, ensure_ascii=False)
