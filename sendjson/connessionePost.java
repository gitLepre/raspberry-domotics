package com.mirenda.luca.homemenager;

import android.os.AsyncTask;
import android.util.Log;
import android.widget.EditText;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

/**
 * Created by Luca on 22/11/2018.
 */

public class connessionePost extends AsyncTask<String, Void, String> {

    String istruzione; //gli passo cosa deve fare la connessione post
    EditText status;
    String risposta;

    public connessionePost(String istruzione, EditText status) {
        this.istruzione = istruzione;
        this.status = status;
    }

    @Override
    protected String doInBackground(String... params) {

        String dati = "";

        HttpURLConnection httpURLConnection = null;
        try {

            httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
            httpURLConnection.setRequestProperty( "Content-Type", "application/x-www-form-urlencoded");
            httpURLConnection.setRequestProperty( "charset", "utf-8");
            httpURLConnection.setRequestMethod("POST");

            httpURLConnection.setDoOutput(true);

            //in base all'istruzione devo passare parametri diversi
            if(istruzione == "accendiLed") {
                String gpio = params[1];
                String token = params[2];

                dati = URLEncoder.encode("gpio", "UTF-8") + "=" + URLEncoder.encode(gpio, "UTF-8");
                dati += "&" + URLEncoder.encode("token", "UTF-8") + "=" + URLEncoder.encode(token, "UTF-8");
            }

            else if (istruzione == "registrati") {

                String username = params[1];
                String password = params[2];
                String id_rasp = params[3];

                dati = URLEncoder.encode("username", "UTF-8") + "=" + URLEncoder.encode(username, "UTF-8");
                dati += "&" + URLEncoder.encode("password", "UTF-8") + "=" + URLEncoder.encode(password, "UTF-8");
                dati += "&" + URLEncoder.encode("id_rasp", "UTF-8") + "=" + URLEncoder.encode(id_rasp, "UTF-8");

            }

            else if (istruzione == "checkToken") {

                String token = params[1];

                dati = URLEncoder.encode("token", "UTF-8") + "=" + URLEncoder.encode(token, "UTF-8");

            }

            OutputStreamWriter wr = new OutputStreamWriter(httpURLConnection.getOutputStream());
            wr.write(dati);
            wr.flush();
            wr.close();

            StringBuilder sb = new StringBuilder();
            String line = null;

            BufferedReader reader = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
            while((line = reader.readLine()) != null) {
                sb.append(line);
                break;
            }

            status.setText(sb.toString());
            risposta = sb.toString();


        } catch (Exception e) {
            e.printStackTrace();
            status.setText("Exception: " + e.toString());
            risposta = e.toString();
        } finally {
            if (httpURLConnection != null) {
                httpURLConnection.disconnect();
            }
        }

        return risposta;
    }

    @Override
    protected void onPostExecute(String result) {
        super.onPostExecute(result);
        Log.e("TAG", result); // this is expecting a response code to be sent from your server upon receiving the POST data

    }
}

