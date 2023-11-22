import collections
import io
import os
from django.http import HttpResponse

import pandas as pd

def read_excel_file(file):
    print(file)
    raw = pd.ExcelFile(file)
    data = {}
    sheets = []
    for sheet_name in raw.sheet_names:
        sheet = raw.parse(sheet_name)
        if 'Tag' in sheet.columns and 'Channel' in sheet.columns and 'I/O Address' in sheet.columns:
            sheet = sheet.dropna(subset=['Tag'])
            data[sheet_name] = sheet
            sheets.append(sheet_name)
        else:
            err = f"This sheet does not contain required columns : {sheet_name}"
            print(err)
    return data, sheets

def create_text_lists(data, text_class, sheet_names, isMurr=False):
    output = io.BytesIO()
    filename = 'IO+Tag' if text_class == 1 else 'Tag' if text_class == 2 else 'IO' if text_class == 3 else 'Ferrules' if text_class == 4 else 'IO+Ferrules'
    writer = pd.ExcelWriter(output)
    df_All_Inputs, df_All_Ouputs = pd.DataFrame(), pd.DataFrame()
    def extract_io_and_tag(row, text_class):
        io_address = row['I/O Address']
        if text_class == 1:
            return f"{io_address} {row['Tag']}"
        elif text_class == 3:
            return io_address
        elif text_class == 4:
            return row['Ferrules']
        elif text_class == 5:
            return f"{io_address} {row['Ferrules']}"
        else:
            return row['Tag']

    for sheet in sheet_names:
        print(f"Creating text lists for sheet {sheet}")

        inputs, outputs = collections.defaultdict(list), collections.defaultdict(list)
        for _, row in data[sheet].iterrows():
            if isMurr:
                inputs[row['Channel']].append(extract_io_and_tag(row, text_class))
                #outputs[1].append(extract_io_and_tag(row, text_class))
            else:
                word = row['I/O Address']
                if "I" in word or 'X' in word:
                    inputs[row['Channel']].append(extract_io_and_tag(row, text_class))
                elif "Q" in word or "O" in word or 'Y' in word:
                    outputs[row['Channel']].append(extract_io_and_tag(row, text_class))

        df_inputs, df_outputs = pd.DataFrame(), pd.DataFrame()

        for i in range(1, int(max(data[sheet]['Channel'])) + 1):
            print(i, inputs[i])
            if inputs:
                df_inputs[i] = pd.DataFrame(inputs[i])
            if outputs:
                df_outputs[i] = pd.DataFrame(outputs[i])
        df_inputs.to_excel(writer, f"Ins_{sheet}")
        df_outputs.to_excel(writer, f"Outs_{sheet}")
        df_All_Inputs = pd.concat([df_All_Inputs, df_inputs])
        df_All_Ouputs = pd.concat([df_All_Ouputs, df_outputs])
        print("Done")
    df_All_Inputs = df_All_Inputs.reset_index(drop= True)
    df_All_Ouputs = df_All_Ouputs.reset_index(drop= True)
    df_All_Inputs.to_excel(writer, "All_Ins")
    df_All_Ouputs.to_excel(writer, "All_Outs")
    writer.close()
    # seek to the beginning of the BytesIO object
    output.seek(0)
    # return the BytesIO object
    return output


# def create_text_lists(data, text_class, sheet_names):
#     output = io.BytesIO()
#     filename = 'IO+Tag' if text_class == 1 else 'Tag' if text_class == 2 else 'IO' if text_class == 3 else 'Ferrules' if text_class == 4 else 'IO+Ferrules'
#     writer = pd.ExcelWriter(output)
#     df_All_Inputs, df_All_Ouputs = pd.DataFrame(), pd.DataFrame()
#     def extract_io_and_tag(row, text_class):
#         io_address = row['I/O Address']
#         if text_class == 1:
#             return f"{io_address} {row['Tag']}"
#         elif text_class == 3:
#             return io_address
#         elif text_class == 4:
#             return row['Ferrules']
#         elif text_class == 5:
#             return f"{io_address} {row['Ferrules']}"
#         else:
#             return row['Tag']
#     for sheet in sheet_names:
#         print(f"Creating text lists for sheet {sheet}")

#         inputs, outputs = collections.defaultdict(list), collections.defaultdict(list)
#         for _, row in data[sheet].iterrows():
#             word = row['I/O Address']
#             if "I" in word :
#             # if word[0] == "I":
#                 inputs[row['Channel']].append(extract_io_and_tag(row, text_class))
#             # elif word[0] == "Q":
#             elif( "Q" in word )or ("O" in word):
#                 outputs[row['Channel']].append(extract_io_and_tag(row, text_class))

#         df_inputs, df_outputs = pd.DataFrame(), pd.DataFrame()


#         for i in range(1, int(max(data[sheet]['Channel'])) + 1):
#             if inputs:
#                 df_inputs[i] = pd.DataFrame(inputs[i])
#             if outputs:
#                 df_outputs[i] = pd.DataFrame(outputs[i])
#         df_inputs.to_excel(writer, f"Ins_{sheet}")
#         df_outputs.to_excel(writer, f"Outs_{sheet}")
#         df_All_Inputs = pd.concat([df_All_Inputs, df_inputs])
#         df_All_Ouputs = pd.concat([df_All_Ouputs, df_outputs])
#         print("Done")
#     df_All_Inputs = df_All_Inputs.reset_index(drop= True)
#     df_All_Ouputs = df_All_Ouputs.reset_index(drop= True)
#     df_All_Inputs.to_excel(writer, f"All_Ins")
#     df_All_Ouputs.to_excel(writer, f"All_Outs")
#     writer.close()
#     # seek to the beginning of the BytesIO object
#     output.seek(0)
#     # return the BytesIO object
#     return output

def create_text_lists8(data, text_class, sheet_names):
    output = io.BytesIO()
    filename = 'IO+Tag' if text_class == 1 else 'Tag' if text_class == 2 else 'IO' if text_class == 3 else 'Ferrules' if text_class == 4 else 'IO+Ferrules'
    writer = pd.ExcelWriter(output)
    df_All_Inputs, df_All_Ouputs = pd.DataFrame(), pd.DataFrame()
    def extract_io_and_tag(row, text_class):
        io_address = row['I/O Address']
        if text_class == 1:
            return f"{io_address} {row['Tag']}"
        elif text_class == 3:
            return io_address
        elif text_class == 4:
            return row['Ferrules']
        elif text_class == 5:
            return f"{io_address} {row['Ferrules']}"
        else:
            return row['Tag']

    for sheet in sheet_names:
        print(f"Creating text lists for sheet {sheet}")

        inputs, outputs = collections.defaultdict(list), collections.defaultdict(list)
        for _, row in data[sheet].iterrows():
            word = row['I/O Address']
            if "I" in word :
            # if word[0] == "I":
                inputs[((row['Channel']- 1) % 8) + 1].append(extract_io_and_tag(row, text_class))
            # elif word[0] == "Q":
            elif( "Q" in word )or ("O" in word):
                outputs[((row['Channel']- 1) % 8) + 1].append(extract_io_and_tag(row, text_class))

        df_inputs, df_outputs = pd.DataFrame(), pd.DataFrame()

        print(inputs)
        for i in range(1, 9): #int(max(data[sheet]['Channel'])) + 1):
            if inputs:
                df_inputs[i] = pd.DataFrame(inputs[i])
            if outputs:
                df_outputs[i] = pd.DataFrame(outputs[i])
        df_inputs.to_excel(writer, f"Ins_{sheet}")
        df_outputs.to_excel(writer, f"Outs_{sheet}")
        df_All_Inputs = pd.concat([df_All_Inputs, df_inputs])
        df_All_Ouputs = pd.concat([df_All_Ouputs, df_outputs])
        print("Done")
    df_All_Inputs = df_All_Inputs.reset_index(drop= True)
    df_All_Ouputs = df_All_Ouputs.reset_index(drop= True)
    df_All_Inputs.to_excel(writer, "All_Ins")
    df_All_Ouputs.to_excel(writer, "All_Outs")
    writer.close()
    # seek to the beginning of the BytesIO object
    output.seek(0)
    # return the BytesIO object
    return output


def createSCL(IBytes,QBytes,IODB):
    text = f"""
// DB Number 1 is used for Inputs
// DB Number 2 is used for Outputs
// DB Number 10 is used for HMI IO
//Output Mapping
IF NOT "HMI_IO".Q_Test_Mode THEN
    POKE_BLK(area_src := 16#84,
             dbNumber_src := 2, //Output DB Number
             byteOffset_src := 0,
             area_dest := 16#82,
             dbNumber_dest := 0,
             byteOffset_dest := 0,
             count := {QBytes});

    //HMI Output Testing mode
ELSE
    POKE_BLK(area_src := 16#84,
             dbNumber_src := {IODB},
             byteOffset_src := 6,
             area_dest := 16#82,
             dbNumber_dest := 0,
             byteOffset_dest := "HMI_IO".IO_Pointer,
             count := 1,
             ENO => ENO);
END_IF;

//HMI Input Status
        POKE_BLK(area_src := 16#84,
                 dbNumber_src := 1,   //Input DB Number
                 byteOffset_src := ("HMI_IO".HMI_IO_Pointer * 2),  // 2 for 16 IOs per screen, 4 for 32 IOs per screen
                 area_dest := 16#84,
                 dbNumber_dest := 10,
                 byteOffset_dest := 2,
                 count := 2,
                 ENO => ENO);

//HMI Output Status
        POKE_BLK(area_src := 16#82,
                 dbNumber_src := 0,
                 byteOffset_src := ("HMI_IO".HMI_IO_Pointer *2),  // 2 for 16 IOs per screen, 4 for 32 IOs per screen
                 area_dest := 16#84,
                 dbNumber_dest := 10,
                 byteOffset_dest := 4,
                 count := 2,
                 ENO => ENO);

//HMI Output for testing Status
        POKE_BLK(area_src := 16#82,
                 dbNumber_src := 0,
                 byteOffset_src := ("HMI_IO".HMI_IO_Pointer),
                 area_dest := 16#84,
                 dbNumber_dest := 10,
                 byteOffset_dest := 7,
                 count := 1,
                 ENO => ENO);
"""
    return io.BytesIO(bytes(text, 'utf-8'))


xml_Header = """<?xml version="1.0" encoding="UTF-8"?>
<alarms version="1.0" product="{E44CB020-C21D-11D3-8A3F-0010A4EF3494}" id="Alarms">
    <alarm history-size="500" capacity-high-warning="90" capacity-high-high-warning="99" display-name="[ALARM]" hold-time="250" max-update-rate="1.00" embedded-server-update-rate="1.00" silence-tag="" remote-silence-exp="" remote-ack-all-exp="" status-reset-tag="" remote-status-reset-exp="" close-display-tag="" remote-close-display-exp="" use-alarm-identifier="false" capacity-high-warning-tag="" capacity-high-high-warning-tag="" capacity-overrun-tag="" remote-clear-history-exp="">
     """
xml_Footer = 	"""</alarm>
</alarms>
"""


def export_to_xml(df):
    # Create an XML-like string from the DataFrame
    triggers_str = "<triggers>\n"
    messages_str = "<messages>\n"

    for _, row in df.iterrows():
        triggers_str += f'    <trigger id="{row["triggerID"]}" type="value" ack-all-value="0" use-ack-all="false" ack-tag="" exp="{{{row["trigger"]}}}" message-tag="" message-handshake-exp="" message-notification-tag="" remote-ack-exp="" remote-ack-handshake-tag="" label="" handshake-tag=""/>\n'

        messages_str += f'    <message id="{row["messageID"]}" trigger-value="1" identifier="1" trigger="#{row["triggerID"]}" backcolor="#800000" forecolor="#FFFFFF" audio="false" display="true" print="false" message-to-tag="false" text="{row["message"]}"/>\n'

    triggers_str += "</triggers>"
    messages_str += "</messages>"

    # Combine the XML strings
    xml_content = xml_Header + '\n' + triggers_str + '\n' + messages_str + '\n' + xml_Footer

    # Return XML content as response
    response = HttpResponse(xml_content, content_type='application/xml')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xml"'

    return response



    


def process_data(file):
    # sourcery skip: extract-duplicate-method, inline-immediately-returned-variable

    # Read the XML-like text file into a DataFrame
    content = file.read().decode('utf-8')

    # Parse the text content to extract data
    triggers_start = content.find("<triggers>")
    triggers_end = content.find("</triggers>")
    triggers_text = content[triggers_start:triggers_end + len("</triggers>")]

    messages_start = content.find("<messages>")
    messages_end = content.find("</messages>")
    messages_text = content[messages_start:messages_end + len("</messages>")]

    triggers_data = {}


    for line in triggers_text.split('\n'):
        if 'trigger id' in line:
            triggerID = line.split('trigger id="')[1].split('"')[0]
            exp = line.split('exp="{')[1].split('}"')[0]
            triggers_data[triggerID] = {'triggerID': triggerID, 'trigger': exp}

    for line in messages_text.split('\n'):
        if 'message id' in line:
            message_id = line.split('message id="')[1].split('"')[0]
            triggerID = line.split('trigger="#')[1].split('"')[0]
            text = line.split('text="')[1].split('"')[0]
            triggers_data[triggerID]['messageID'] = message_id
            triggers_data[triggerID]['message'] = text

    triggers_df = pd.DataFrame(triggers_data)
    print(triggers_df)
    triggers_df = triggers_df.transpose()
    print(triggers_df)

    # Create Excel content in memory
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        triggers_df.to_excel(writer, sheet_name='Triggers', index=False)

    excel_buffer.seek(0)

    # Set response headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=output.xlsx'

    # Write Excel content to the response
    response.write(excel_buffer.read())

    return response

