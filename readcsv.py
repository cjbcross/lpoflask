# from sas7bdat import SAS7BDAT
#
# def return_rest(cust_id):
#     # print "In readcsv - cust_id: " + cust_id
#     with SAS7BDAT('exception_recommendations.sas7bdat') as f:
#         df = f.readlines()
#         for item in df:
#             if unicode(cust_id) in unicode(item[0]):
#                 print item
#     #     df = f.to_data_frame()
#     #     df_final = df.loc[df['CTM_ID'] == int(cust_id)]
#     #     df_final['Details'] = '<a href="/chart.html?segmentid=' + df_final['SegmentID'].apply(str) + '&level=' + df_final['Level'].apply(str) + '">See details</a>'
#     #
#     # return df_final.to_json(orient='records')
#
#
# return_rest(5)


import pandas as pd

def return_rest(cust_id):
    df = pd.read_csv('exception_recommendations.csv')
    df['Details'] = '<a href="/chart.html?segmentid='+df['SegmentID'].apply(str)+'&level='+df['Level'].apply(str)+'">See details</a>'
    print cust_id
    return df.ix[df['CTM_ID'] == int(cust_id)].to_json(orient='records')
