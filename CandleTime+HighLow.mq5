//+------------------------------------------------------------------+
//|                                                   candleTime.mq5 |
//|                   Francesco Danti Copyright 2011, OracolTech.com |
//|                                       http://blog.oracoltech.com |
//|                                      email:     fdanti@gmail.com |
//+------------------------------------------------------------------+
#property copyright "Francesco Danti Copyright 2011, OracolTech.com"
#property link      "http://blog.oracoltech.com"
#property version   "1.00"

#property indicator_chart_window

#property indicator_buffers 1
#property indicator_plots   1

string idxLabel="lblNextCandle";

input color lblColor=Red;                    // Color of the label
input int fontSize=15;                                // Size of the label font
input ENUM_ANCHOR_POINT pAnchor = ANCHOR_LEFT_LOWER; // Anchor of the label a sort of a
 bool nextToPriceOrAnchor = true;               // Position near the price close or to Corner
input ENUM_BASE_CORNER pCorner = CORNER_LEFT_LOWER;  // Corner position of the label
input string fontFamily = "Tahoma";                  // Font family of the label
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
int OnInit()
  {
   return(0);
  }
//+------------------------------------------------------------------+
//| Custom indicator deinitialization function                       |
//+------------------------------------------------------------------+
void OnDeinit(const int r)
  {
   Comment("");
   ObjectDelete(0,idxLabel);
   ObjectsDeleteAll(0,-1,-1);
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
   ArraySetAsSeries(time,true);
   ArraySetAsSeries(close,true);

   int idxLastBar=rates_total-1;
   int tS,iS,iM,iH;
   string sS,sM,sH;

   tS=(int) time[0]+PeriodSeconds() -(int) TimeCurrent();

   iS=tS%60;

   iM=(tS-iS);
   if(iM!=0) iM/=60;
   iM-=(iM-iM%60);

   iH=(tS-iS-iM*60);
   if(iH != 0) iH /= 60;
   if(iH != 0) iH /= 60;

   sS = IntegerToString(iS,2,'0');
   sM = IntegerToString(iM,2,'0');
   sH = IntegerToString(iH,2,'0');

   string cmt=sH+":"+sM+":"+sS;
      double hig=iHigh(NULL,0,(iHighest(NULL,0,MODE_HIGH,6,0)));
      double lower =iLow(NULL,0,(iLowest(NULL,0,MODE_LOW,6,0)));
      double bid=SymbolInfoDouble(Symbol(),SYMBOL_BID); 
  
   if(nextToPriceOrAnchor)
     {
      if(ObjectGetInteger(0,idxLabel,OBJPROP_TYPE)==OBJ_LABEL) ObjectDelete(0,idxLabel);
      ObjectCreate(0,idxLabel,OBJ_TEXT,0,time[0]+PeriodSeconds()*1,close[0]);
      ObjectSetInteger(0,idxLabel,OBJPROP_ANCHOR,pAnchor);
     }
   else
     {
      if(ObjectGetInteger(0,idxLabel,OBJPROP_TYPE)==OBJ_TEXT) ObjectDelete(0,idxLabel);
      ObjectCreate(0,idxLabel,OBJ_LABEL,0,0,0);
      ObjectSetInteger(0,idxLabel,OBJPROP_ANCHOR,pAnchor);
      ObjectSetInteger(0,idxLabel,OBJPROP_CORNER,pCorner);
     }


   ObjectSetInteger(0,idxLabel,OBJPROP_COLOR,lblColor);
   ObjectSetString(0,idxLabel,OBJPROP_TEXT,cmt);
   ObjectSetInteger(0,idxLabel,OBJPROP_FONTSIZE,fontSize);
   ObjectSetString(0,idxLabel,OBJPROP_FONT,fontFamily);
   
   
   ObjectCreate(0,"Trendiz", OBJ_LABEL, 0, 0, 0);
      ObjectSetString(0,"Trendiz",OBJPROP_TEXT," High - Bid = ");
      ObjectSetInteger(0,"Trendiz", OBJPROP_CORNER, 3);
      ObjectSetInteger(0,"Trendiz", OBJPROP_XDISTANCE, 300);
      ObjectSetInteger(0,"Trendiz", OBJPROP_YDISTANCE, 10);
      ObjectSetInteger(0,"Trendiz", OBJPROP_FONTSIZE, 15);
      ObjectSetInteger(0,"Trendiz", OBJPROP_COLOR, Red);

      
      ObjectCreate(0,"Trendz", OBJ_LABEL, 0, 0, 0);
      ObjectSetString(0,"Trendz",OBJPROP_TEXT,NormalizeDouble(hig-bid,2));
      ObjectSetInteger(0,"Trendz", OBJPROP_CORNER, 3);
      ObjectSetInteger(0,"Trendz", OBJPROP_XDISTANCE, 100);
      ObjectSetInteger(0,"Trendz", OBJPROP_YDISTANCE, 10); 
      ObjectSetInteger(0,"Trendz", OBJPROP_FONTSIZE, 15); 
      ObjectSetInteger(0,"Trendz", OBJPROP_COLOR, Red); 
//------
   ObjectCreate(0,"Trendiz1", OBJ_LABEL, 0, 0, 0);
      ObjectSetString(0,"Trendiz1",OBJPROP_TEXT," Bid - Low = ");
      ObjectSetInteger(0,"Trendiz1", OBJPROP_CORNER, 3);
      ObjectSetInteger(0,"Trendiz1", OBJPROP_XDISTANCE, 300);
      ObjectSetInteger(0,"Trendiz1", OBJPROP_YDISTANCE, 50);
      ObjectSetInteger(0,"Trendiz1", OBJPROP_FONTSIZE, 15);
      ObjectSetInteger(0,"Trendiz1", OBJPROP_COLOR, Lime);

      
      ObjectCreate(0,"Trendz1", OBJ_LABEL, 0, 0, 0);
      ObjectSetString(0,"Trendz1",OBJPROP_TEXT,NormalizeDouble(bid-lower,2));
      ObjectSetInteger(0,"Trendz1", OBJPROP_CORNER, 3);
      ObjectSetInteger(0,"Trendz1", OBJPROP_XDISTANCE, 100);
      ObjectSetInteger(0,"Trendz1", OBJPROP_YDISTANCE, 50); 
      ObjectSetInteger(0,"Trendz1", OBJPROP_FONTSIZE, 15); 
      ObjectSetInteger(0,"Trendz1", OBJPROP_COLOR, Lime); 
      
//------
 //  ObjectCreate(0,"Trendiz12", OBJ_LABEL, 0, 0, 0);
  //    ObjectSetString(0,"Trendiz12",OBJPROP_TEXT," Next-Candle = ");
  //    ObjectSetInteger(0,"Trendiz12", OBJPROP_CORNER, 0);
  //    ObjectSetInteger(0,"Trendiz12", OBJPROP_XDISTANCE, 190);
  //    ObjectSetInteger(0,"Trendiz12", OBJPROP_YDISTANCE, 50);
  //    ObjectSetInteger(0,"Trendiz12", OBJPROP_FONTSIZE, 15);
  //    ObjectSetInteger(0,"Trendiz12", OBJPROP_COLOR, Yellow);

      
   //   ObjectCreate(0,"Trendz12", OBJ_LABEL, 0, 0, 0);
   //   ObjectSetString(0,"Trendz12",OBJPROP_TEXT,cmt);
   //   ObjectSetInteger(0,"Trendz12", OBJPROP_CORNER, 0);
   //   ObjectSetInteger(0,"Trendz12", OBJPROP_XDISTANCE, 330);
   //   ObjectSetInteger(0,"Trendz12", OBJPROP_YDISTANCE, 50); 
    //  ObjectSetInteger(0,"Trendz12", OBJPROP_FONTSIZE, 15); 
    //  ObjectSetInteger(0,"Trendz12", OBJPROP_COLOR, Yellow);       
      
   return(rates_total);
  }
//+------------------------------------------------------------------+
