# IMPORTING ALL THE NECESSARY LIBRARIES


import datetime
import webbrowser
import wikipedia
import random
import os
import requests
from gtts import gTTS
import speech_recognition as sr
import playsound
import urllib

#________________________________________

#DEFINING THE REQUIRED VARIABLES

wake = "ok python"
boolean = True
saved_f = list(range(1,1000))
ran1 = random.choice(saved_f)
rand = random.choice(saved_f)
sites_list = ['youtube.com', '17,773,093', '100', '2', 'www.google.com', '12,121,415', '100', '3', 'apple.com', '4,599,135', '100', '4', 'docs.google.com', '2,264,343', '99', '5', 'www.blogger.com', '25,228,854', '99', '6', 'support.google.com', '4,567,382', '99', '7', 'play.google.com', '2,378,037', '99', '8', 'microsoft.com', '4,494,110', '99', '9', 'adobe.com', '2,878,836', '98', '10', 'maps.google.com', '4,401,467', '98', '11', 'wordpress.org', '9,908,954', '98', '12', 'cloudflare.com', '5,216,383', '98', '13', 'plus.google.com', '11,986,046', '98', '14', 'linkedin.com', '8,845,452', '98', '15', 'en.wikipedia.org', '5,492,548', '98', '16', 'accounts.google.com', '2,534,221', '97', '17', 'vimeo.com', '3,129,499', '97', '18', 'europa.eu', '1,687,296', '97', '19', 'sites.google.com', '1,687,085', '97', '20', 'mozilla.org', '1,956,554', '97', '21', 'drive.google.com', '1,786,378', '97', '22', 'googleusercontent.com', '2,161,440', '97', '23', 'youtu.be', '3,946,670', '97', '24', 'facebook.com', '45,613,803', '96', '25', 'amazon.com', '4,022,134', '96', '26', 'line.me', '596,838', '96', '27', 'github.com', '2,012,694', '96', '28', 'bp.blogspot.com', '15,947,816', '96', '29', 'vk.com', '1,600,588', '96', '30', 'medium.com', '1,130,428', '96', '31', 'bbc.co.uk', '1,425,853', '96', '32', 'es.wikipedia.org', '779,618', '96', '33', 'istockphoto.com', '3,087,381', '96', '34', 'creativecommons.org', '1,553,255', '96', '35', 'whatsapp.com', '1,730,132', '95', '36', 'jimdofree.com', '1,659,976', '95', '37', 'networkadvertising.org', '705,213', '95', '38', 'google.fr', '383,359', '95', '39', 'ok.ru', '330,607', '95', '40', 'feedburner.com', '1,750,883', '95', '41', 'nytimes.com', '1,696,124', '95', '42', 'theguardian.com', '1,206,115', '95', '43', 'google.co.jp', '631,246', '95', '44', 'mail.google.com', '440,230', '95', '45', 'photos.google.com', '232,792', '95', '46', 'aliexpress.com', '442,946', '95', '47', 'w3.org', '1,067,418', '95', '48', 'gstatic.com', '585,535', '95', '49', 't.me', '510,291', '95', '50', 'slideshare.net', '877,838', '95', '51', 'developers.google.com', '906,715', '95', '52', 'uol.com.br', '562,399', '95', '53', 'fr.wikipedia.org', '540,271', '95', '54', 'nih.gov', '1,058,842', '95', '55', 'www.yahoo.com', '913,997', '95', '56', 'pt.wikipedia.org', '359,480', '95', '57', 'policies.google.com', '1,099,082', '95', '58', 'cnn.com', '1,232,808', '95', '59', 'bbc.com', '677,028', '95', '60', 'news.google.com', '687,492', '95', '61', 'hugedomains.com', '5,058,423', '95', '62', 'wikimedia.org', '1,371,372', '95', '63', 'google.de', '1,093,367', '95', '64', 'forbes.com', '1,097,898', '95', '65', 'live.com', '738,686', '95', '66', 'who.int', '2,232,274', '95', '67', 'dropbox.com', '940,317', '95', '68', 'buydomains.com', '1,148,596', '95', '69', 'google.es', '415,035', '95', '70', 'dailymotion.com', '1,072,286', '95', '71', 'paypal.com', '908,923', '95', '72', 'google.com.br', '264,690', '95', '73', 'imdb.com', '1,236,625', '95', '74', 'google.co.uk', '545,026', '95', '75', 'msn.com', '991,511', '95', '76', 'myspace.com', '1,260,457', '95', '77', 'reuters.com', '735,895', '95', '78', 'globo.com', '385,337', '95', '79', 'mail.ru', '481,599', '95', '80', 'opera.com', '758,501', '94', '81', 'booking.com', '355,658', '94', '82', 'un.org', '422,787', '94', '83', 'harvard.edu', '591,885', '94', '84', 'hatena.ne.jp', '1,457,165', '94', '85', 'office.com', '348,744', '94', '86', 'news.yahoo.com', '576,011', '94', '87', 'pinterest.com', '7,164,685', '94', '88', 'telegraph.co.uk', '780,628', '94', '89', 'thesun.co.uk', '256,893', '94', '90', 'elpais.com', '326,493', '94', '91', 'fandom.com', '431,080', '94', '92', 'bit.ly', '4,032,441', '94', '93', 'google.it', '411,263', '94', '94', 'steampowered.com', '218,378', '94', '95', 'bing.com', '891,779', '94', '96', 'dailymail.co.uk', '784,988', '94', '97', 'oracle.com', '529,310', '94', '98', 'ebay.com', '886,625', '94', '99', 'ft.com', '355,037', '94', '100', 'cpanel.com', '1,245,159', '94', '101', 'get.google.com', '565,350', '94', '102', 'huffingtonpost.com', '884,730', '94', '103', 'rt.com', '232,483', '94', '104', 'nasa.gov', '553,487', '94', '105', 'washingtonpost.com', '875,958', '94', '106', 'aboutads.info', '490,911', '94', '107', 'independent.co.uk', '524,315', '94', '108', 'files.wordpress.com', '1,989,260', '94', '109', 'mediafire.com', '766,721', '94', '110', 'www.gov.uk', '487,297', '94', '111', 'time.com', '620,570', '94', '112', 'cdc.gov', '659,910', '94', '113', 'amazon.co.jp', '773,715', '94', '114', 'samsung.com', '307,757', '94', '115', 'wikia.com', '463,302', '94', '116', 'wsj.com', '809,538', '94', '117', 'ipv4.google.com', '353,592', '94', '118', 'tools.google.com', '1,501,287', '94', '119', 'code.google.com', '323,703', '94', '120', 'sedo.com', '2,388,721', '94', '121', 'goo.gl', '4,200,596', '94', '122', 'change.org', '395,648', '94', '123', 'gravatar.com', '1,777,311', '94', '124', 'youronlinechoices.com', '515,154', '94', '125', 'www.wix.com', '897,207', '94', '126', 'search.google.com', '969,626', '94', '127', 'bloomberg.com', '673,994', '94', '128', 'telegram.me', '270,829', '94', '129', 'amazon.de', '494,150', '94', '130', 'webmd.com', '551,806', '94', '131', 'marketingplatform.google.com', '749,205', '94', '132', 'mirror.co.uk', '260,164', '94', '133', 'rakuten.co.jp', '589,940', '94', '134', 'cpanel.net', '1,332,426', '94', '135', 'terra.com.br', '187,094', '94', '136', 'privacyshield.gov', '420,544', '94', '137', 'twitter.com', '48,377,685', '94', '138', 'abcnews.go.com', '476,955', '94', '139', 'plesk.com', '697,680', '94', '140', 'tinyurl.com', '1,231,745', '94', '141', 'namecheap.com', '808,020', '94', '142', 'google.ru', '173,216', '94', '143', 'de.wikipedia.org', '596,109', '94', '144', 'foxnews.com', '455,981', '94', '145', 'picasaweb.google.com', '615,457', '94', '146', 'android.com', '267,068', '94', '147', 'translate.google.com', '276,606', '94', '148', 'archive.org', '883,296', '94', '149', 'amazon.co.uk', '632,993', '94', '150', 'cnet.com', '552,564', '94', '151', 'businessinsider.com', '580,793', '94', '152', 'books.google.com', '348,351', '94', '153', 'abril.com.br', '227,794', '94', '154', 'issuu.com', '844,623', '94', '155', 'ig.com.br', '133,072', '94', '156', 'aol.com', '654,184', '94', '157', 'fb.com', '354,540', '94', '158', 'soundcloud.com', '1,566,367', '94', '159', 'myaccount.google.com', '264,940', '94', '160', 'lefigaro.fr', '182,626', '94', '161', 'picasa.google.com', '248,802', '94', '162', 'themeforest.net', '508,782', '94', '163', 'wired.com', '539,677', '94', '164', 'draft.blogger.com', '7,924,357', '94', '165', 'usatoday.com', '640,078', '94', '166', 'scribd.com', '649,666', '94', '167', 'netflix.com', '245,873', '93', '168', 'storage.googleapis.com', '445,411', '93', '169', 'lg.com', '120,580', '93', '170', 'nationalgeographic.com', '535,739', '93', '171', 't.co', '1,706,312', '93', '172', 'mit.edu', '572,405', '93', '173', 'orkut.com.br', '120,198', '93', '174', 'imageshack.com', '436,382', '93', '175', 'bitly.com', '308,393', '93', '176', 'pbs.org', '425,136', '93', '177', 'bloglovin.com', '442,956', '93', '178', 'sciencemag.org', '267,175', '93', '179', 'digg.com', '818,014', '93', '180', 'sciencedirect.com', '423,399', '93', '181', 'usnews.com', '327,283', '93', '182', 'mega.nz', '151,740', '93', '183', 'urbandictionary.com', '208,235', '93', '184', 'bt.com', '172,846', '93', '185', 'alibaba.com', '372,597', '93', '186', 'engadget.com', '402,060', '93', '187', 'umich.edu', '296,707', '93', '188', 'php.net', '626,096', '93', '189', 'deezer.com', '124,726', '93', '190', 'google.pl', '188,594', '93', '191', 'asus.com', '141,033', '93', '192', 'express.co.uk', '205,495', '93', '193', 'ja.wikipedia.org', '329,615', '93', '194', 'loc.gov', '371,484', '93', '195', 'blackberry.com', '135,944', '93', '196', 'disqus.com', '922,027', '93', '197', 'news.com.au', '253,540', '93', '198', 'pl.wikipedia.org', '128,845', '93', '199', 'lemonde.fr', '225,450', '93', '200', '4shared.com', '507,799', '93', '201', 'tes.com', '398,720', '93', '202', 'welt.de', '160,073', '93', '203', 'spiegel.de', '266,227', '93', '204', 'nicovideo.jp', '138,641', '93', '205', 'imageshack.us', '788,507', '93', '206', 'disney.com', '212,486', '93', '207', 'dan.com', '1,472,083', '93', '208', 'eventbrite.com', '545,681', '93', '209', 'wikihow.com', '350,233', '93', '210', 'stanford.edu', '514,714', '93', '211', 'rambler.ru', '231,907', '93', '212', 'washington.edu', '311,102', '93', '213', 'forms.gle', '331,933', '93', '214', 'twitch.tv', '298,937', '93', '215', 'smh.com.au', '264,641', '93', '216', 'nbcnews.com', '307,922', '93', '217', 'mystrikingly.com', '248,406', '93', '218', 'adssettings.google.com', '302,514', '93', '219', 'trustpilot.com', '318,474', '93', '220', 'academia.edu', '286,200', '93', '221', 'cisco.com', '209,219', '93', '222', 'biglobe.ne.jp', '224,462', '93', '223', 'hollywoodreporter.com', '216,977', '93', '224', 'ovh.co.uk', '567,292', '93', '225', 'surveymonkey.com', '384,970', '93', '226', 'naver.jp', '129,828', '93', '227', 'asahi.com', '163,529', '93', '228', 'shopify.com', '1,209,746', '93', '229', 'abc.net.au', '326,546', '93', '230', 'ggpht.com', '573,740', '93', '231', 'amazon.fr', '219,761', '93', '232', 'yelp.com', '808,870', '93', '233', 'ign.com', '233,560', '93', '234', 'it.wikipedia.org', '285,573', '93', '235', 'pixabay.com', '299,666', '93', '236', 'yandex.ru', '917,678', '93', '237', 'walmart.com', '268,164', '93', '238', 'vox.com', '380,753', '93', '239', 'rapidshare.com', '282,624', '93', '240', 'e-recht24.de', '446,236', '93', '241', 'wiley.com', '439,757', '93', '242', 'wa.me', '408,388', '93', '243', 'berkeley.edu', '391,518', '93', '244', 'google.co.id', '134,855', '93', '245', 'cbsnews.com', '431,229', '93', '246', 'indiatimes.com', '336,655', '93', '247', 'gnu.org', '573,090', '93', '248', 'iubenda.com', '183,132', '93', '249', 'parallels.com', '583,444', '93', '250', 'nginx.com', '458,344', '93', '251', 'dw.com', '221,745', '93', '252', '000webhost.com', '283,603', '93', '253', 'ria.ru', '155,795', '93', '254', 'pexels.com', '143,912', '93', '255', 'guardian.co.uk', '524,125', '93', '256', 'www.weebly.com', '332,312', '93', '257', 'my.yahoo.com', '1,133,646', '93', '258', 'cbc.ca', '351,007', '93', '259', 'spotify.com', '1,110,447', '93', '260', 'huffpost.com', '417,973', '93', '261', 'addtoany.com', '707,532', '93', '262', 'scoop.it', '337,140', '93', '263', 'vice.com', '305,182', '93', '264', 'xbox.com', '145,830', '93', '265', 'nginx.org', '543,884', '93', '266', 'finance.yahoo.com', '373,233', '93', '267', 'ox.ac.uk', '221,475', '93', '268', 'dell.com', '210,999', '93', '269', 'icann.org', '387,169', '93', '270', 'bandcamp.com', '509,057', '93', '271', 'mashable.com', '346,066', '93', '272', 'gmail.com', '182,616', '93', '273', 'a8.net', '422,800', '93', '274', 'amazon.it', '126,083', '93', '275', 'm.wikipedia.org', '229,815', '93', '276', 'sciencedaily.com', '291,252', '93', '277', 'akamaihd.net', '413,891', '93', '278', 'depositfiles.com', '140,685', '93', '279', 'whitehouse.gov', '318,596', '93', '280', 'thetimes.co.uk', '300,157', '93', '281', 'google.nl', '217,933', '93', '282', 'bp1.blogger.com', '522,027', '93', '283', 'addthis.com', '700,904', '93', '284', 'theatlantic.com', '427,949', '93', '285', 'elmundo.es', '193,370', '93', '286', 'sapo.pt', '206,750', '93', '287', 'naver.com', '417,447', '93', '288', 'yale.edu', '282,508', '93', '289', 'worldbank.org', '205,531', '93', '290', 'goodreads.com', '666,510', '93', '291', 'id.wikipedia.org', '409,452', '93', '292', 'xinhuanet.com', '636,725', '93', '293', 'hm.com', '155,073', '93', '294', 'columbia.edu', '278,533', '93', '295', 'quora.com', '307,872', '93', '296', 'detik.com', '350,228', '93', '297', 'nydailynews.com', '304,613', '93', '298', 'gizmodo.com', '342,746', '93', '299', 'wp.com', '921,045', '93', '300', 'weibo.com', '1,492,563', '93', '301', 'photobucket.com', '1,584,138', '93', '302', 'stackoverflow.com', '284,597', '93', '303', 'oup.com', '315,622', '93', '304', 'qq.com', '4,177,713', '93', '305', 'amazon.es', '145,210', '93', '306', 'ikea.com', '265,457', '93', '307', 'rtve.es', '143,223', '93', '308', 'ea.com', '158,821', '93', '309', 'cambridge.org', '223,141', '93', '310', 'princeton.edu', '282,881', '93', '311', 'ietf.org', '354,134', '93', '312', 'nikkei.com', '188,987', '93', '313', 'nypost.com', '291,689', '93', '314', 'nvidia.com', '147,102', '93', '315', 'hp.com', '393,343', '93', '316', 'doubleclick.net', '649,477', '93', '317', 'unesco.org', '255,567', '93', '318', 'metro.co.uk', '177,487', '93', '319', 'ibm.com', '441,713', '93', '320', 'nature.com', '445,503', '93', '321', 'cnbc.com', '399,915', '93', '322', 'godaddy.com', '2,312,204', '93', '323', 'secureserver.net', '904,953', '93', '324', 'cornell.edu', '372,031', '93', '325', 'gofundme.com', '274,317', '93', '326', 'bp0.blogger.com', '521,977', '93', '327', 'photos1.blogger.com', '820,985', '93', '328', 'sendspace.com', '151,301', '93', '329', 'espn.com', '298,311', '93', '330', 'tripadvisor.com', '449,866', '93', '331', 'newsweek.com', '248,306', '93', '332', 'ovh.net', '715,418', '93', '333', 'ytimg.com', '244,138', '93', '334', 'techcrunch.com', '394,950', '93', '335', 'abc.es', '158,112', '93', '336', 'mysql.com', '406,755', '93', '337', 'economist.com', '305,903', '93', '338', 'shutterstock.com', '250,806', '93', '339', 'nhk.or.jp', '206,944', '93', '340', 'apache.org', '888,594', '93', '341', 'ru.wikipedia.org', '356,612', '93', '342', 'www.over-blog.com', '586,239', '93', '343', 'fifa.com', '144,087', '93', '344', 'netvibes.com', '1,150,303', '93', '345', 'standard.co.uk', '146,614', '93', '346', 'goo.ne.jp', '298,643', '93', '347', 'noaa.gov', '283,981', '93', '348', 'yadi.sk', '173,196', '93', '349', 'instagram.com', '20,490,897', '93', '350', 'latimes.com', '580,966', '93', '351', 'channel4.com', '144,979', '93', '352', 'researchgate.net', '320,834', '93', '353', 'windowsphone.com', '123,495', '93', '354', 'over-blog-kiwi.com', '155,788', '93', '355', 'theverge.com', '304,008', '93', '356', 'buzzfeed.com', '450,187', '93', '357', 'box.com', '232,607', '93', '358', 'kickstarter.com', '409,165', '93', '359', 'about.com', '674,842', '93', '360', 'britannica.com', '270,189', '93', '361', 'instructables.com', '274,749', '93', '362', 'yahoo.co.jp', '621,888', '93', '363', 'bp2.blogger.com', '522,355', '93', '364', 'google.com.tw', '127,556', '93', '365', 'list-manage.com', '621,938', '93', '366', 'psychologytoday.com', '274,824', '93', '367', 'ted.com', '482,161', '93', '368', 'nokia.com', '160,553', '93', '369', 'variety.com', '200,965', '93', '370', 'groups.google.com', '301,610', '93', '371', 'sfgate.com', '320,344', '93', '372', 'zendesk.com', '446,514', '93', '373', 'google.co.in', '245,753', '93', '374', 'playstation.com', '181,623', '93', '375', 'utexas.edu', '234,121', '93', '376', 'googleblog.com', '216,776', '93', '377', 'ovh.com', '405,938', '93', '378', 'www.wikipedia.org', '530,366', '93', '379', 'npr.org', '601,849', '93', '380', 'google.ca', '294,180', '93', '381', 'marriott.com', '332,335', '93', '382', 'so-net.ne.jp', '174,673', '92', '383', 'corriere.it', '143,805', '92', '384', 'axs.com', '224,976', '92', '385', 'airbnb.com', '167,494', '92', '386', 'excite.co.jp', '485,874', '92', '387', 'etsy.com', '1,499,041', '92', '388', 'stuff.co.nz', '137,953', '92', '389', 'amazon.in', '134,864', '92', '390', 'marketwatch.com', '285,398', '92', '391', 'mozilla.com', '200,172', '92', '392', 'rottentomatoes.com', '197,191', '92', '393', 'prnewswire.com', '304,666', '92', '394', 'sina.com.cn', '1,129,875', '92', '395', 'orange.fr', '167,133', '92', '396', 'dictionary.com', '239,211', '92', '397', 'intel.com', '226,881', '92', '398', 'cbslocal.com', '270,925', '92', '399', 'ask.fm', '239,811', '92', '400', 'narod.ru', '272,214', '92', '401', 'daum.net', '158,206', '92', '402', 'e-monsite.com', '141,294', '92', '403', 'feedproxy.google.com', '755,375', '92', '404', 'mail.yahoo.com', '170,062', '92', '405', 'espn.go.com', '227,356', '92', '406', 'archives.gov', '215,223', '92', '407', 'softonic.com', '133,130', '92', '408', 'usc.edu', '188,857', '92', '409', 'disney.go.com', '167,448', '92', '410', 'dot.tk', '6,051,637', '92', '411', 'scientificamerican.com', '249,335', '92', '412', 'teamviewer.com', '149,493', '92', '413', 'psu.edu', '271,048', '92', '414', 'debian.org', '336,076', '92', '415', 'www.skyrock.com', '10,744,472', '92', '416', 'thefreedictionary.com', '193,139', '92', '417', 'gesetze-im-internet.de', '136,026', '92', '418', 'chicagotribune.com', '299,914', '92', '419', 'cmu.edu', '204,528', '92', '420', 'pcmag.com', '189,780', '92', '421', 'www.livejournal.com', '2,861,494', '92', '422', 'history.com', '189,405', '92', '423', 'uber.com', '121,808', '92', '424', 'chinadaily.com.cn', '278,260', '92', '425', 'mercurynews.com', '161,510', '92', '426', 'fortune.com', '217,643', '92', '427', 'lonelyplanet.com', '152,885', '92', '428', 'plos.org', '222,191', '92', '429', 'venturebeat.com', '180,320', '92', '430', 'weather.com', '214,196', '92', '431', 'chron.com', '196,128', '92', '432', 'ed.gov', '237,981', '92', '433', 'target.com', '228,864', '92', '434', 'ca.gov', '376,671', '92', '435', 'mixcloud.com', '172,072', '92', '436', 'fastcompany.com', '257,712', '92', '437', 'merriam-webster.com', '234,524', '92', '438', 'techradar.com', '129,146', '92', '439', 'inc.com', '209,201', '92', '440', '20minutos.es', '122,048', '92', '441', 'sky.com', '186,743', '92', '442', 'bp3.blogger.com', '522,244', '92', '443', 'politico.com', '208,199', '92', '444', 'lego.com', '121,790', '92', '445', 'nifty.com', '215,014', '92', '446', 'stores.jp', '406,999', '92', '447', 'people.com', '197,664', '92', '448', 'home.pl', '202,434', '92', '449', 'usgs.gov', '196,963', '92', '450', 'statista.com', '184,545', '92', '451', 'consumerreports.org', '149,595', '92', '452', 'flickr.com', '8,545,919', '92', '453', 'tmz.com', '178,477', '92', '454', 'amazon.ca', '176,955', '92', '455', 'huawei.com', '125,129', '92', '456', 'ucla.edu', '229,735', '92', '457', 'sports.yahoo.com', '177,957', '92', '458', 'video.google.com', '204,708', '92', '459', 'elsevier.com', '224,532', '92', '460', 'mayoclinic.org', '275,880', '92', '461', 'nba.com', '181,454', '92', '462', 'ssl-images-amazon.com', '156,420', '92', '463', 'boston.com', '279,039', '92', '464', 'dreamstime.com', '131,514', '92', '465', 'upenn.edu', '266,375', '92', '466', 'clickbank.net', '430,366', '92', '467', 'businesswire.com', '231,826', '92', '468', 'geocities.jp', '244,495', '92', '469', 'autodesk.com', '126,265', '92', '470', 'foursquare.com', '237,812', '92', '471', 'ftc.gov', '216,040', '92', '472', 'softpedia.com', '161,541', '92', '473', 'unicef.org', '139,989', '92', '474', 'sakura.ne.jp', '363,947', '92', '475', 'biblegateway.com', '206,920', '92', '476', 'repubblica.it', '172,386', '92', '477', 'howstuffworks.com', '260,260', '92', '478', 'ap.org', '179,217', '92', '479', 'evernote.com', '257,577', '92', '480', 'com.com', '229,664', '92', '481', 'interia.pl', '158,168', '92', '482', 'soratemplates.com', '196,042', '92', '483', 'outlook.com', '192,409', '92', '484', 'oreilly.com', '222,053', '92', '485', 'rediff.com', '268,938', '92', '486', 'gooyaabitemplates.com', '326,704', '92', '487', 'gutenberg.org', '159,907', '92', '488', 'ebay.co.uk', '205,883', '92', '489', 'jstor.org', '153,834', '92', '490', 'iso.org', '171,091', '92', '491', 'indiegogo.com', '217,498', '92', '492', 'fb.me', '231,633', '92', '493', 'arxiv.org', '178,866', '92', '494', 'alexa.com', '285,827', '92', '495', 'thoughtco.com', '295,267', '92', '496', 'billboard.com', '165,710', '92', '497', 'ucoz.ru', '184,459', '92', '498', 'mhlw.go.jp', '138,334', '92', '499', 'enable-javascript.com', '915,622', '92', '500', 'newscientist.com']

#_________________________________________



# DEFINING ALL THE REQUIRED FUNCTIONS

def say(text):
    tts = gTTS(text=text,lang='en')
    filename = f"{rand}.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(f"{rand}.mp3")

def get_audio():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.listen(source,phrase_time_limit=5,timeout=10)
        said = ""
        
            
        said = r.recognize_google(audio_data)
            
        
            
    return said.lower()

def getWeatherData(cityName):
    api = 'http://api.openweathermap.org/data/2.5/weather?appid=c6db7752bda2accb8b608e3f44e534f5&q='
    url = api + cityName

    data = requests.get(url).json()
    weatherCondition = data['weather'][0]['main']
    temp = data['main']['temp']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    windSpeed = data['wind']['speed']
    
    print(f"The weather is {weatherCondition}, and the temperature is {temp} kelvin. Atmospheric Pressure is around {pressure}. The humidity is {humidity}, while the windspeed is {windSpeed}")
    say(f"The weather is {weatherCondition}, and the temperature is {temp} kelvin. Atmospheric Pressure is around {pressure}. The humidity is {humidity}, while the windspeed is {windSpeed}")
    

def wikisearch(title):
    results = wikipedia.summary(title,sentences=2)
    print(results)
    say(results)
    
def siteOpener(siteName):
    for i in range(0,len(sites_list)):
        try:
            if siteName in sites_list[i]:
                webbrowser.open("https://"+sites_list[i])
                break
        except Exception as e :
            say(f" An error occured. {e}")
            
def timeFinder():
    time = datetime.datetime.now()
    say("It is ,"+str(time)[11:16])
    
def dateFinder():
    date = datetime.datetime.now()
    say("Today is,"+str(date)[0:10])
 
def google_search(search_var):
    que = "https://google.com/?#q="
    webbrowser.open(que+search_var,new=2)
         
def make_note(note):
    file=open(f"Note{ran1}.txt",'w')
    file.write(note)
    file.close()
    print(note)
    say('done')
#___________________________________________

# THE MAIN FUNCTION

def main_function():
    
    if 'search wikipedia' in speech:
        say("What do you want to search on Wikipedia")
        search_que = get_audio()
        wikisearch(search_que)
    
    elif 'time' in speech:
        timeFinder()
        
    elif 'date' in speech:
        dateFinder()
    
    elif  'make a note' in speech:
        say('Ok tell, what do you want to write in the note.')
        to_be_noted = get_audio()
        make_note(to_be_noted)
        say("done")
    
    elif 'search google' in speech:
        say('What do you want to search on google')
        data1 = get_audio()
        google_search(data1)
    
    elif 'open a site' in speech:
        say('Which site do you want to open')
        sitename = get_audio()
        siteOpener(sitename)
    
    elif 'who are you' in speech:
        say('I am your. Assistant python')
        
    elif 'weather' or 'temperature' in speech:
        say("Which city")
        city = get_audio()
        getWeatherData(city)
       
# The main method runs here

while boolean:
    speech1 = get_audio()
    
    if wake in speech1:
        say("Yes tell me what to do")
        speech = get_audio()
        print(speech)
        main_function()
        
    elif 'shutdown python' in speech1:
        say("Bye Bye baccha. Have a nice day")
        boolean = False
        break


        
    
    
    
            
#_____________________________________________________________________________________________________________________________
