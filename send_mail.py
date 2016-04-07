#!/usr/bin/python
import re
import os
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders


class Prepender:
    def __init__(self, fname, mode='w'):
        self.__write_queue = []
        self.__f = open(fname, mode)

    def write(self, s):
        self.__write_queue.insert(0, s)

    def close(self):
        self.__exit__(None, None, None)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.__write_queue:
            self.__f.writelines(self.__write_queue)
        self.__f.close()


# sends an email..
def send_mail(send_from, send_to, subject, text, file, server="localhost"):
    # assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    if file is not None:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(file.read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file.name))
        file.close()
        msg.attach(part)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    email_sender = "internal-notifier@baysensors.com"
    email_passwd = "qrltz112798317"
    smtp.login(email_sender, email_passwd)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


if __name__ == '__main__':
    cwd = os.getcwd()
    email_list = open(cwd + "/fill_holes/email_receipt_list.txt", "r")
    email_receipt = email_list.read().splitlines()
    print email_receipt

    target_day = datetime.date.fromordinal(datetime.date.today().toordinal() - 2).strftime('%Y-%m-%d')
    print 'Check the data hole for ' + target_day
    with open(cwd + '/fill_holes/data_hole_summary2.csv') as f:
        lines = f.readlines()
    total_hour = 0
    hole_hour = 0
    detail = list()
    for line in lines:
        fields = re.split(',', line)
        if fields[0] == target_day:
            total_hour += float(fields[7])
            hole_hour += float(fields[8])
            if float(fields[8]) > 0.0:
                content = ",".join(fields[2:]) + "\n"
                detail.append(content)

                # print detail
    hole_percentage = hole_hour / total_hour
    with open(cwd + '/fill_holes/datahole_record2.txt', 'r+') as record:
        content = record.read()
        record.seek(0, 0)
        record.write(str(hole_percentage * 100).rstrip('\r\n') + '\n' + content)
    avg_7days = 0
    count = 0
    for hole in open(cwd + '/fill_holes/datahole_record2.txt'):
        if hole.strip() == "":
            continue
        avg_7days += float(hole)
        count += 1
        if count == 7:
            break
    avg_7days /= count
    report_message = 'Data hole for ' + target_day + ' is: ' + "{0:.2f}%".format(hole_percentage * 100) + \
                     '[%s/%s]' % (hole_hour, total_hour) + '\n\n7 Days average is ' + "{0:.2f}%".format(avg_7days) \
                     + '[%s/%s]' % (avg_7days, count) + '\n'
    detail.insert(0, report_message)

    # zone_count_holes_info
    attach = None

    # attach error file
    if os.path.isfile(cwd + '/fill_holes/errors.txt'):
        attach = open(cwd + '/fill_holes/errors.txt', 'rb')
    try:
        send_mail("internal-notifier@baysensors.com", email_receipt, "Deployed Device Data Hole Report", '\n'.join(detail),
              attach, server="localhost")
    finally:
        if attach:
            attach.close()
        if os.path.isfile(cwd + '/fill_holes/errors.txt'):
            os.remove(cwd + '/fill_holes/errors.txt')

