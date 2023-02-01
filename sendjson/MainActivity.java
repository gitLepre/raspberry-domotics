package com.example.luca.sendjson;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText status = findViewById(R.id.status);


        Button submitButton = (Button) findViewById(R.id.submit_button);

        submitButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                try {
                JSONArray listGpio = new JSONArray();
                listGpio.put("18");
                listGpio.put("22");

                JSONObject postData = new JSONObject();

                    postData.put("notifica","True");
                    postData.put("gpio",listGpio);
                    postData.put("token", "111aaa");


                    new inviaJson().execute("https://af078cd8.ngrok.io/presenza", postData.toString());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        });

        Button inviaButton = (Button) findViewById(R.id.accendi_button);
        inviaButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                    String gpio = "18";
                    String token = "111aaa";

                    new accendi(status).execute("https://af078cd8.ngrok.io/gpio", gpio,token);

            }
        });
    }
}
