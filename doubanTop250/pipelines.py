class Doubantop250Pipeline:
    def process_item(self, item, spider):
        with open('top250.txt', 'a', encoding='utf8') as fp:
            fp.write(item['name']+'\n')
            fp.write(item['director'].strip().split(' ')[1]+'\n')
            fp.write(item['brief'].strip()+'\n')
            fp.write(item['score']+'\n')
            fp.write(item['comment'][:-3]+'\n')
            if len(item['quote'])==1:
                fp.write(item['quote'][0]+'\n')
            else:
                fp.write('\n')
        return item
