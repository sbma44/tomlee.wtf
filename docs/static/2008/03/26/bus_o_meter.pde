#define DIMENSIONS 2

#define SERIAL_ECHO true

int times_index = 0;
long wmata_times[2*DIMENSIONS];
long record_times[DIMENSIONS];
long lastFlash = 0;
int pin_index[DIMENSIONS] = {9,11};
int red_pin_index[DIMENSIONS] = {7,6};
bool RECEPTION = false;

void SetIllumination(int bank, int value)
{
  if(bank==0)
  {
    digitalWrite(4,value);
    digitalWrite(5,value);
  }
  else if(bank==1)
  {
    digitalWrite(2,value);
    digitalWrite(3,value);
  }  
}

void SetAllIllumination(int value)
{
  SetIllumination(0,value);
  SetIllumination(1,value);
}

void FlashLEDs(int count)
{
  for(int i=0;i<count;i++)
  {
    // flash LEDs
    SetAllIllumination(LOW);
    delay(250);
    SetAllIllumination(HIGH);
    delay(250);
  }
}

void setup()
{
  // initialize amber LEDs
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  
  // initialize red LEDs
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  
  // initial LED flash
  FlashLEDs(2);
  
  
  // zero meters
  for(int i=0;i<DIMENSIONS;i++)
  {
    analogWrite(pin_index[i],0);
  }
  
  // serial
  Serial.begin(9600);
  pinMode(11,OUTPUT);
  pinMode(9, OUTPUT);
  Serial.println("Starting up...");
}

void loop()
{
  if (Serial.available() > 0) 
  {
    int incoming = Serial.read();
    if(((char)incoming)=='#')
    {
      //Serial.println("detected beginning of number");
      long current_time = 0;
      for(int i=5;i>=0;i--)
      {      
        while(Serial.available()==0)
        {
          delay(100);
        }
        int incoming = Serial.read();
        if((incoming>=48) && (incoming<=57))
        {       
          incoming = incoming - 48;
          current_time = current_time + (incoming * pow(10,i));
        }
        else
        {
          current_time = -1;
          break;
        }
      }  
            
      if(current_time!=-1)
      {
        RECEPTION = true;
        wmata_times[times_index] = current_time;
        record_times[(int) floor(times_index/2)] = floor(millis() / 1000);
        times_index = (times_index + 1) % (2*DIMENSIONS);
        
        // debug
        Serial.print("Detected number: ");
        Serial.println(current_time);
      }         
    }    
        
    if(SERIAL_ECHO==true)
    {
      Serial.print((char) incoming);    
    }
  }
  
    
  // flash lights periodically if we haven't received anything (and it's been long enough since the last flash)
  if(!RECEPTION)
  {
    if(((((int)(millis()/1000.0) % 5))==0) && (millis()>(lastFlash+2000)))
    {
      FlashLEDs(1);
      lastFlash = millis();
    }
  }
  // if we have received something, calculate what we should display
  else
  {
    for(int i=0;i<DIMENSIONS;i++)
    {
      int walking_time_left = max(0,(wmata_times[(i*2)+1] - ((millis()/1000) - record_times[i])));
      int display_value = floor(255.0 * max(0,((wmata_times[i*2] - ((millis()/1000) - record_times[i])) / (40*60.0))));
     
      // set the needle
      display_value = min(display_value, 250);      
      analogWrite(pin_index[i],display_value);
      
      // enable amber backlighting if walking time is left
      SetIllumination(i,((walking_time_left>0) ? LOW : HIGH));

      // enable red backlighting if less than a minute of walking time is left
      digitalWrite(red_pin_index[i],((walking_time_left<=60) ? LOW : HIGH));
    }
  }

}
