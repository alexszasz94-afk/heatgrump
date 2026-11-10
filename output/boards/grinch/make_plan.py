import json,re
base=json.load(open('/tmp/pp/grinch-living-r4.json'))[0]['params']['prompt']
# rebuild retry5 prompt exactly as submitted
o1="THE BACK OF THE HOOD is exactly like Image 4: red velvet with the floppy Santa tip and the white fluffy pompom clearly visible on the back when the hood hangs down her back."
n1="WHEN THE HOOD HANGS DOWN HER BACK (shot 1): it lies flat and neat between her shoulder blades, exactly like Image 4 and Image 5: red velvet with the white fluffy pompom, and at the top of the hanging hood the green plush panel with the Grinch face is turned outward and clearly visible from behind: the two big yellow Grinch eyes with black pupils and the black heavy eyebrows, framed by the white sherpa border."
p=base
o2=p[p.index("THE FOOT POCKETS"):p.index("\nSHOT 1")]
n2="THE FOOT POCKETS are built exactly like Image 6 and Image 7: two deep green velvet pockets with a white fluffy band on top, sewn together side by side across the whole width at the inside of the hem, joined in the middle in a W shape; one piece, never separate booties, never slippers, never boots. Each foot goes DEEP inside its pocket exactly like Image 7: the green pocket fabric covers the whole foot and the ankle, the white band of the pocket sits at mid-shin height, and the bottom of the pocket with the foot inside rests flat on the floor; the foot is never visible below, under or beside the pocket."
o3="SHOT 1 (0 to 1.13 s): seen from behind, exactly like the input, she swings the robe onto her shoulders; we see her back and the back of the robe exactly like Image 4, the hood down on her back with the Santa tip and the white pompom clearly visible; her face is not seen."
n3="SHOT 1 (0 to 1.13 s): seen from behind, exactly like the input, she puts the robe on her shoulders in one smooth, natural movement; the robe keeps its real shape exactly like Image 4 (red top, black belt, green bottom down to the floor), never twisted, never flying, never deformed; the hood hangs neatly down her back with the green Grinch face, its yellow eyes and the white pompom clearly visible; her face is not seen."
o4=p[p.index("Both feet go INTO the pockets"):p.index("\nLOOK")]
n4="Both feet go deep INTO the pockets and stay inside until the end; once a foot is inside it never comes out again; at the end the closed robe rests on the floor and her feet are completely hidden inside the pockets: no foot, no sock, no heel and no toe is ever visible below the hem."
for o,n in [(o1,n1),(o2,n2),(o3,n3),(o4,n4)]: p=p.replace(o,n)
BR=p
ROOM_OLD=BR[BR.index("ROOM: "):BR.index(" ROBE: ")]
HAIR_OLD="(long wavy dark-blonde hair)"
PJ_OLD="very cute lime-green and red Christmas plaid pajamas with long sleeves and long pants"
assert ROOM_OLD and HAIR_OLD in BR and PJ_OLD in BR

G={"01":("9a37133b-0a2d-4ea5-8192-b0266f2bd887","long wavy blonde hair"),
"02":("17f4d19c-bd12-4b5b-b946-21f85411dc52","long straight dark-brown hair"),
"03":("5fdb82c7-13eb-4cf4-a5c8-5b66b2cb55ce","shoulder-length wavy copper-red hair"),
"04":("01e4de96-bc33-43b3-a885-46ca1205a7f5","light-brown hair in a half-up ponytail"),
"05":("7cbc86d4-f362-4fde-bf85-e8a4805db11f","short straight platinum-blonde bob"),
"06":("63b1f1a7-b572-413e-891f-5c815b03f6e6","long wavy brunette hair"),
"07":("4027c35a-6799-4897-b4de-e02ce2d5735e","long straight black hair"),
"08":("bfb600a0-1f19-4c62-b2be-f72ae23f6a1a","long wavy dark-blonde hair"),
"09":("ea2406c5-98c3-4de4-a063-38433ea32250","shoulder-length wavy auburn-red hair"),
"10":("5214f5d9-1501-465c-989b-b8f95e3eb1c4","long straight brown hair")}
# room: id, kind, broll room text, cozy seat text, behind text
R={
"01":("4e8d9822-e02c-4886-8f02-ec727d72c219","B","the white bed with the lime-green fluffy throw and the red pom-pom pillows, the Grinch Christmas tree with the red-and-white striped top, the window with the sunset, the white wall shelves with a lime-green fluffy stocking, the dark dresser with the lamp, and the white fluffy rug","the red pom-pom pillows and the lime-green fluffy pillows of the bed are directly behind her back, and the lime-green fluffy throw lies on the bed beside her","the window with white curtains and the sunset outside, and the Grinch Christmas tree with the red-and-white striped top"),
"02":("8511a5be-ab5b-4eea-89c1-5b21c1d4d662","B","the white bed with the red and green pillows and the green knit throw, the wreath with the red-and-white striped bow, the fairy lights on the wall, the window with the sunset, the nightstand with the lamp, the Christmas tree with red-and-white striped ribbons on the right, and the white fluffy rug","the red pillows and the green pillows of the bed are directly behind her back, and the green knit throw lies on the bed beside her","the wreath with the red-and-white striped bow, the fairy lights, the window with white curtains and the sunset outside, and the lamp"),
"03":("c75d9e4d-0d8f-4e26-b316-ca5d7a20c0db","B","the white bed with the lime-green fluffy pillows, the two red Santa-hat pillows and the lime-green fluffy throw, the tall slim Christmas tree in front of the window with the sunset, the nightstand with the lamp, and the white fluffy rug","the lime-green fluffy pillows and the two red Santa-hat pillows of the bed are directly behind her back, and the lime-green fluffy throw lies on the bed beside her","the headboard, the lamp, and the tall slim Christmas tree in front of the window with the sunset"),
"04":("f4a1e75d-6de4-42af-b3e5-ff1c6f650720","B","the white bed with the green and patterned pillows and the green knit throw, the pine garland and the wreath on the wall above the bed, the window with the sunset, the dark nightstand with the lamp, the Christmas tree with the green gifts on the right, and the white fluffy rug","the green, patterned and white pillows of the bed are directly behind her back, and the green knit throw lies on the bed beside her","the pine garland and the wreath on the wall, the window with white curtains and the sunset outside, and the Christmas tree"),
"05":("8835ed6b-7d07-4620-9f36-cd0fa389a242","B","the white bed with the olive-green and burgundy pillows, the window with blinds and the sunset, the shelf with little red and green trees and burgundy bows, the nightstand with the lamp, the Christmas tree with burgundy bows and the peppermint ornament on top, and the white fluffy rug","the olive-green and burgundy pillows of the bed are directly behind her back, and the white duvet is all around her","the window with blinds and the sunset outside, the shelf with the burgundy bows, the lamp, and the Christmas tree with burgundy bows"),
"06":("50ea7199-8ef7-4864-84e1-02075e699e06","L","the white fireplace with the lime-green fluffy stockings, the Grinch Christmas tree with the red-and-white striped top, the window with the sunset, the round cream sofa with its pillows and red throw, and the plain light wooden floor with NO rug","the sofa's backrest with the lime-green fluffy pillow and the red pillow with white pompom trim is directly behind her back, and the red knit throw hangs over the front of the sofa next to her","the tall window with white curtains and the sunset outside, and the Grinch Christmas tree with the red-and-white striped top at the left end of the sofa"),
"07":("41473b05-210d-4027-b8bc-04c243cff4fd","L","the white fireplace with the fire and the garland, the big winter painting, the Grinch Christmas tree with red-and-white striped ribbons and a curled top, the window with the sunset, the round cream boucle sofa on the right with a green pillow, a red pillow, a red-and-white peppermint pillow and the green knit throw, and the plain light wooden floor with NO rug","the sofa's backrest with the green pillow, the red pillow and the red-and-white peppermint pillow is directly behind her back, and the green knit throw hangs over the front of the sofa next to her","the window with white curtains and the sunset outside, the lamp, and the Grinch Christmas tree with red-and-white striped ribbons at the left end of the sofa"),
"08":("7c8f3cae-fee4-43a8-871d-97e65621068a","L","the white fireplace with the two white knit stockings, the winter painting, the flocked white Christmas tree with red and green ornaments and a curled top, the tall window with the sunset, the round cream boucle sofa on the right with red pillows with white pompoms, a green pillow, a white fur throw and a green fur throw, and the light grey rug on the light wooden floor","the sofa's backrest with the red pillows with white pompoms and the green pillow is directly behind her back, and the white fur throw and the green fur throw lie on the sofa next to her","the tall window with white curtains and the sunset outside, and the flocked white Christmas tree at the left end of the sofa"),
"09":("a62fea19-d0b7-4525-b4ce-6e0c6df65f4f","L","the white fireplace with the green stocking and the garland, the winter river painting, the Christmas tree with red and green ornaments, the tall window with the sunset, the round cream boucle sofa on the right with a green pillow, a floral pillow and the green knit throw, and the plain light floor with NO rug","the sofa's backrest with the green pillow and the floral pillow is directly behind her back, and the green knit throw hangs over the front of the sofa next to her","the tall window with white curtains and the sunset outside, and the Christmas tree with red and green ornaments at the left end of the sofa"),
"10":("5e9d73ff-8547-4e34-a0e5-2c2a5cabd22e","L","the white fireplace with the fire, the red bow and the garland, the winter painting, the Grinch Christmas tree with red bows and the red-and-white striped top, the window with the sunset and the lamp, the round cream boucle sofa on the right with a red velvet pillow, a green pillow and the red knit throw, the light rug, and the bowl of red and green ornaments","the sofa's backrest with the red velvet pillow and the green pillow is directly behind her back, and the red knit throw hangs over the front of the sofa next to her","the window with white curtains and the sunset outside, the lamp, and the Grinch Christmas tree with red bows at the left end of the sofa"),
}

import re as _re
_pp=json.load(open('/home/user/heatgrump/output/boards/printesa/plan.json'))
PR={}
for _s in _pp:
    _r=_s['room']
    if _r in PR: continue
    PR[_r]=(_s['cozy']['medias'][2]['value'],_re.search(r'PLACE: (.*?) ROBE:',_s['cozy']['prompt']).group(1))
for _r,(_id,_pl) in PR.items():
    R["P"+_r]=(_id,"PL","its fireplace, Christmas tree, window and sofa"+(" and the soft grey rug" if _r=="10" else ""),_pl,"")
PJ=["very cute lime-green and red Christmas plaid pajamas with long sleeves and long pants",
"very cute red flannel Christmas pajamas with tiny white snowflakes, long sleeves and long pants",
"very cute lime-green Christmas pajamas with red cuffs and tiny white stars, long sleeves and long pants"]
SETS=[("G1",1,"08","06"),("G1",2,"01","02"),("G1",3,"05","P06"),
("G2",1,"06","01"),("G2",2,"02","07"),("G2",3,"10","P07"),
("G3",1,"03","03"),("G3",2,"07","08"),("G3",3,"04","P08"),
("G4",1,"09","05"),("G4",2,"10","P09"),("G4",3,"02","03"),
("G5",1,"07","01"),("G5",2,"05","10"),("G5",3,"06","P10")]
REFS=["ccf9632e-bffd-46a1-9f7d-407a8a1bb79f","26930d56-68f4-445c-9d43-ebb4c1c7d438","dfb3995b-c326-4495-a226-bc212e60dabf","7d7c5351-bf61-46fe-b5b7-903d6d4223e8","2cb89cc9-7866-419a-84b1-968d69c361e6"]
COMMON="24bae836-2c4a-48e0-89b6-49fcc0b21612"
def broll(g,r,pj):
    gid,hair=G[g]; rid,kind,rtxt,_,_=R[r]
    kw="bedroom" if kind=="B" else "living room"
    room=f"ROOM: exactly the {kw} of Image 2, only what is in Image 2: {rtxt}, all in their real places, soft warm evening light; "
    if kind=="PL": room=f"ROOM: exactly the living room of Image 2, only what is in Image 2, with {rtxt} in their real places, soft warm evening light; never add or invent furniture"+(", rugs or carpets." if "rug" not in rtxt else ".")
    elif True: room+= "she stands on the white fluffy rug in front of the bed; never add or invent furniture." if kind=="B" else ("never add or invent furniture, rugs or carpets." if "NO rug" in rtxt else "never add or invent furniture.")
    t=BR.replace(ROOM_OLD,room).replace(HAIR_OLD,f"({hair})").replace(PJ_OLD,PJ[pj])
    return {"model":"kling4_0","mode":"video-edit","duration":5,"resolution":"1080p","aspect_ratio":"9:16","declined_preset_id":COMMON,
      "medias":[{"role":"video_references","value":"0f47593e-9893-4d61-9546-904f540027d1"}]+[{"role":"image_references","value":v} for v in [gid,rid]+REFS],"prompt":t}
HOOD="THE HOOD UP on her head, every detail exactly like Image 4: red velvet Santa-hat hood with the long floppy tip and the big white fluffy pompom, the green plush panel on its front with the Grinch's yellow eyes, black heavy eyebrows and small dark nose, green plush inside, thick white sherpa border; the hood sits back on her head, its front edge above her eyebrows, so her own eyes and whole face are clearly visible in every frame, never covered or shaded by the hood."
TAIL="The robe is very thick, puffy and cozy, extra fluffy. THE ROBE IS CLOSED: the belt is tied and the two front panels overlap completely from her neck down to the floor, wrapped tightly over her lap, her knees and her legs; there is never any gap or opening between the panels. HER LEGS ARE NEVER SEEN: no bare leg, no knee, no shin, no ankle, no sock, no foot and no pajama is visible at any moment - only the green robe fabric covers her from the waist to the floor and its white hem rests on the floor over her feet. "
def cozy(g,r):
    gid,hair=G[g]; rid,kind,_,seat,behind=R[r]
    if kind=="PL":
        place="PLACE: "+seat
        light="the lamps and the sunset window"; act="she sits down on the sofa, hood up, and hugs herself inside the warm robe, smiling."
    elif kind=="B":
        place=f"PLACE: the bedroom of Image 2 exactly as it is, filmed close to the bed. She sits ON THE BED OF IMAGE 2, on top of its white duvet, exactly like the woman in the input video sits on her sofa: the soft white mattress and duvet are under her, {seat}. There is no stool, no pouf, no ottoman, no bench, no chair and no sofa anywhere; nothing stands in front of the bed; she is never in the middle of the room. Never add, move or invent furniture and never change the bed. Behind the bed is what is really there in Image 2: {behind}."
        light="the lamp and the sunset window"; act="she sits down, hood up, and hugs herself inside the warm robe, smiling."
    else:
        place=f"PLACE: the living room of Image 2 exactly as it is. She sits ON THE ROUND CREAM BOUCLE SOFA OF IMAGE 2, exactly like the woman in the input video sits on her sofa: the sofa's seat cushion is under her, {seat}. There is no pouf, no ottoman, no stool, no armchair and no round seat anywhere; she is never in the middle of the room. Never add, move or invent furniture and never change the sofa. Behind the sofa is what is really behind it in Image 2: {behind}."
        light="the fireplace and the sunset window"; act="she sits down on the sofa, hood up, and hugs herself inside the warm robe, smiling."
    t=(f"Edit the input video. Keep EXACTLY the same movement, framing and timing as the input video, second by second: {act} Change only the person, the place and the robe. PERSON: exactly the woman of Image 1, same face and hair ({hair}), her whole face visible. {place} ROBE: the Grinch robe of Image 3 (front) and Image 4 (hood), reproduced one to one: red plush velvet upper part, green plush velvet lower part, thick white fluffy sherpa trims, fluffy lime-green fur cuffs, black belt TIED closed at her waist. {HOOD} {TAIL}"
       f"LOOK: a real unedited iPhone 16 video in a real home, completely realistic, very soft warm natural light from {light}, gentle low contrast, no HDR, no glow, no CGI. Natural movement, no morphing, correct hands with five fingers. NO TEXT: no captions, no emoji, no watermark, no logos. Silent.")
    return {"model":"kling4_0","mode":"video-edit","duration":3,"resolution":"1080p","aspect_ratio":"9:16","declined_preset_id":COMMON,
      "medias":[{"role":"video_references","value":"258676d7-ae40-431d-a10b-29fe42f3ebd7"}]+[{"role":"image_references","value":v} for v in [gid,rid,REFS[0],REFS[2]]],"prompt":t}
plan=[]
for i,(a,n,g,r) in enumerate(SETS):
    plan.append({"id":f"{a}-{n}","account":a,"girl":g,"room":r,"kind":R[r][1],"broll":broll(g,r,i%3),"cozy":cozy(g,r)})
plan[0]["done"]={"broll":"135552_988d81dd-2324-4f4e-a090-b2de00250dc0","cozy":"133144_ea748687-496e-4898-bd5f-9c9a67d72cac","cozy_start":0.6}
plan[3]["reuse_cozy"]="db42542f-0d40-4dff-a8c0-26fec996543b"
json.dump(plan,open('/home/user/heatgrump/output/boards/grinch/plan.json','w'),indent=1)
print(plan[1]["broll"]["prompt"][:1500]); print(); print(plan[4]["cozy"]["prompt"])
