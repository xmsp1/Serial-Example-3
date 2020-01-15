int nums1[]={568,529,750,627,743,434};
int nums2[]={98,111,120,84,89,136};
float nums3[]={25.40,36.50,42.30,27.60,28.00,24.65};
float nums4[]={-25.40,-36.50,-42.30,-27.60,-28.00,-24.65};
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(3,OUTPUT);
}

void loop() {

  for (int i=0;i<6;i++){
    //Serial.println();
    Serial.println(nums1[i]);
    
    delay(200);
    Serial.println(nums2[i]);
    delay(200);
    Serial.println(nums3[i]);
    delay(200);

    }
    
}
