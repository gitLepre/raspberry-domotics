package com.mirenda.luca.homemenager;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class accendiActivity extends AppCompatActivity  {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.accendi);
    }

    public void accendiGpio(View v){
        String gpio = v.getTag().toString();
        String token = "111aaa";
        final EditText status = findViewById(R.id.status);
        final EditText url = findViewById(R.id.url);

        String urltxt = url.getText().toString();
        //new accendi(status).execute("https://8abb207b.ngrok.io/gpio", gpio,token);
        new connessionePost("accendiLed",status).execute(urltxt+"/gpio", gpio,token);
    }

    public void jsonPresenza(View v) throws ExecutionException, InterruptedException {
        final EditText status = findViewById(R.id.status);
        try {
            JSONArray listGpio = new JSONArray();
            listGpio.put("18");
            listGpio.put("22");

            JSONObject postData = new JSONObject();

            postData.put("notifica","True");
            postData.put("gpio",listGpio);

            String token = "111aaa";
            final EditText url = findViewById(R.id.url);

            String urltxt = url.getText().toString();

            String risposta =  new connessionePost("checkToken", status).execute(urltxt+"/tokenSensore", token).get();
            status.setText(risposta);

            if(risposta.equals("true"))
                new inviaJson(status).execute(urltxt+"/presenza", postData.toString());

        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

    public void jsonTemperatura(View v){
        final EditText status = findViewById(R.id.status);
        try {
            JSONArray listGpio = new JSONArray();
            listGpio.put("18");
            listGpio.put("27");

            JSONObject postData = new JSONObject();


            postData.put("gpio",listGpio);
            postData.put("token", "111aaa");
            postData.put("min", "24");
            postData.put("max", "28");

            final EditText url = findViewById(R.id.url);

            String urltxt = url.getText().toString();
            new inviaJson(status).execute(urltxt+"/temperatura", postData.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
