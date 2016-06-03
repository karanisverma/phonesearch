import re
from lxml import html

p = re.compile(ur'\s*\r\n|\r|\n')
storage_and_ram_regex = re.compile(ur'(\d{1,3})\sgb,\s(\d{1})\sgb')
camera_regex = re.compile(ur'\d+\smp')
battery_regex = re.compile(ur'\d+\smah')


def parse_feature(body):
    '''Parse the responce'''
    # list of allowed features which needs to be stored
    specs = ['batter', 'camera', 'ram', 'storage']
    mobile_data = {}
    for i in range(len(body)):
        clear_val = map(lambda x: re.sub(p, "", x), body[i])
        # clear_val = map((lambda x: x.replace('\r\n', "")), r[i])
        clear_val = [j.lower() for j in clear_val if j is not ""]
        clear_val = " ".join(clear_val)
        clear_val = " ".join(clear_val.split())
        if any(x in clear_val for x in specs):
            # print clear_val
            if 'battery' in clear_val:
                # print clear_val
                search = re.search(battery_regex, clear_val)
                if search:
                    # print "battery => ",search.group(0)
                    mobile_data['battery'] = search.group(0)

            if 'camera' in clear_val:
                # UPDATE HERE WITH BATTERY LOGIC
                # print clear_val
                search = re.search(camera_regex, clear_val)
                if search:
                    mobile_data['camera'] = search.group(0)
                # print "camera => ",re.search(camera_regex,clear_val).group(0)

            if 'ram' in clear_val:
                # print clear_val
                search = re.findall(storage_and_ram_regex, clear_val)
                if search:
                    temp_ram = []
                    temp_storeage = []
                    for i in search:
                        temp_ram.append(i[1])
                        temp_storeage.append(i[0])
                    mobile_data['ram'] = temp_ram
                    mobile_data['storage'] = temp_storeage
    return mobile_data


def split_product(mobile_name, mobile_image, url, mobile_data):
    mobile_list = []
    if len(mobile_data['ram']) and len(mobile_data['storage']):
        for m in range(len(mobile_data['ram'])):
            temp_mobile_data = {}
            temp_mobile_data = mobile_data.copy()
            temp_mobile_data['name'] = mobile_name[0]
            temp_mobile_data['url'] = url
            temp_mobile_data['img'] = mobile_image[0]
            temp_mobile_data['ram'] = mobile_data['ram'][m]
            temp_mobile_data['storage'] = mobile_data['storage'][m]
            mobile_list.append(temp_mobile_data)
        return mobile_list

# mdata = parse_feature(r)
# split_product(mdata)



def content_parser(content, url):
    try:
        # DEBUGGING CODE
        # if content:
        #     return content
        # else:
        #     print "other content => ", content
        #     print "url is => ",url

        # BEAUTYFULSOUP 
        # soup = BeautifulSoup(content)
        # table = soup.find(id = "specs-list")
        # if table:
        #     # return table
        #     rows = table.findAll('tr')
        #     for r in rows:
        #         print r

        tree = html.fromstring(content)
        ram = []
        key = (tree.xpath('//td[@class="ttl"]/a/text()'))
        mobile_name = (tree.xpath('//h1[@class="specs-phone-name-title"]/text()'))
        mobile_image= (tree.xpath('//div[@class="specs-photo-main"]/a/img/@src'))
        # values = (tree.xpath('//td[@class="info"]/a/text()'))
        row = (tree.xpath('//div[@id="specs-list"]//tr'))
        if row:
            row = [i.xpath('descendant-or-self::text()')for i in row]
        # product_name = [i.xpath('descendant-or-self::text()')
        #                 for i in product_name]
        # print "##############################################"
        # print "KEY ===> ", key
        # print "Value =>>> ", values
        # print "----------------------------------------------"
        # print "Row ==>> ", row
        mdata = parse_feature(row)
        # print mdata
        mobile_list = split_product(mobile_name, mobile_image, url, mdata)
        return mobile_list
        # print content
        # print "##############################################"
    except Exception,e:
        # print "----------------------------------------------"
        # print "ERROR"
        # print "----------------------------------------------"
        pass
        # print "XXXXXXXXXXXXXXXXXXXXX BROKEN HTML XXXXXXXXXXXXXXXXXXXXXXXXX"
    return None
