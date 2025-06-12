import pandas as pd

MAPPINGS = [
    {
        "Video_name": "ox4tIwVNzsc.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "143",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "sFPL3aoCBVQ.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "430",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "0NV1KdWRHck",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "1071",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "QhMO5SSmiaA.mp4",
        "no of speaker": "1",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "351",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "9OvibwfflDg.mp4",
        "no of speaker": "1",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "662",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "B1Uv91Xvdno.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "694",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "pX2zvfD6GCY.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "384",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "TZ0aPN78k6E.mp4",
        "no of speaker": "4",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "1298",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "zRxqMVRtgw8.mp4",
        "no of speaker": "3",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "871",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "PaVJS3Uqa60.mp4",
        "no of speaker": "3",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "872",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "g99avxNMeTw.mp4",
        "no of speaker": "2",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "641",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "lea-Wl_uWXY.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "426",
        "content/speaker": "content_speaker",
        "has captions": "no"
    },
    {
        "Video_name": "3dQ6yKSttEc.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "3258",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "6a4W8oSMjl4.mp4",
        "no of speaker": "1",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "528",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "ZKi97irvUkQ.mp4",
        "no of speaker": "2",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "228",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "0vaySkIQips.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "81",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "Bl5630CeYFs.mp4",
        "no of speaker": "1",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "453",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "3sik096fGg0.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "58",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "i40oXOjETAM.mp4",
        "no of speaker": "3",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "567",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "yr3CS01dzjU.mp4",
        "no of speaker": "2",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "818",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "T5OlEM7pfC4.mp4",
        "no of speaker": "3",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "55",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "Fpnic1EJJjE.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "872",
        "content/speaker": "content_speaker",
        "has captions": "no"
    },
    {
        "Video_name": "xIH6fIsONE4.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "647",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "vFmjgbdNNgw.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "834",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "fCNuPcf8L00.mp4",
        "no of speaker": "1",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "899",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "YmjIiDjVQ1c.mp4",
        "no of speaker": "2",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "60",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "X60DPGODWC4.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "27",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "psb7bt1IfnA.mp4",
        "no of speaker": "4",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "49",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "1obYOEMYw8E.mp4",
        "no of speaker": "5",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "54",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "RCT9KIKbAUY.mp4",
        "no of speaker": "4",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "199",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "7Xe2yhUJfHY.mp4",
        "no of speaker": "3",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "240",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "ibTwzWSY5KI.mp4",
        "no of speaker": "3",
        "speaker's moment": "moving",
        "lang support": "en",
        "clip duration(sec)": "59",
        "content/speaker": "speaker",
        "has captions": "yes"
    },
    {
        "Video_name": "yMX81NnWijQ.mp4",
        "no of speaker": "2",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "122",
        "content/speaker": "speaker",
        "has captions": "no"
    },
    {
        "Video_name": "-7ZmDHudOEM.mp4",
        "no of speaker": "4",
        "speaker's moment": "steady",
        "lang support": "en",
        "clip duration(sec)": "235",
        "content/speaker": "speaker",
        "has captions": "no"
    }
]

def get_video_paths(min_time=0, max_time=3600):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(MAPPINGS)
    
    # Convert 'clip duration(sec)' to numeric, coercing errors
    df['clip duration(sec)'] = pd.to_numeric(df['clip duration(sec)'], errors='coerce')
    
    # Filter the DataFrame based on the clip duration
    filtered_df = df[(df['clip duration(sec)'] >= min_time) & (df['clip duration(sec)'] <= max_time)]
    
    # Strip leading and trailing whitespace from 'Video_name'
    filtered_df['Video_name'] = filtered_df['Video_name'].str.strip()
    
    # Return the list of video paths
    paths = filtered_df['Video_name'].tolist()
    paths = [f'/home/vedantpatel/clipit_video_dataset/downloaded/{path}' for path in paths]
    return paths
