package com.mirenda.luca.homemenager;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class RegisterFormActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register_form);
        final EditText userText = findViewById(R.id.userText);

    }

    public void changeActivity(View view) {

        Intent intent = new Intent(this, accendiActivity.class);
        startActivity(intent);

    }

    public void changeActivity2(View view) {

        Intent intent = new Intent(this, sensorePresenza.class);
        startActivity(intent);

    }

    public void registrati(View view) {
        EditText userText = findViewById(R.id.userText);
        String user = userText.getText().toString();

        EditText passText = findViewById(R.id.passText);
        String pass = passText.getText().toString();

        EditText raspText = findViewById(R.id.idRasp);
        String idRasp = raspText.getText().toString();

        EditText status = findViewById(R.id.status);
        new connessionePost("registrati",status)
                .execute("http://webdev.dibris.unige.it/~S4254186/tesi/php/registrati.php",user,pass,idRasp);

    }
}
