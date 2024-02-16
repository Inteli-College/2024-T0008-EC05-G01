import React from "react";
import styles from "../css/profile.module.css";

export const Membro = ({nome, imagem, linkedin}) => (
    <div className= {styles.profile_container} >
        <img src={imagem} alt={nome} className={styles.image}/>
        <div className={styles.text_container}>
            <p className={styles.name}>{nome}</p>
            <p className={styles.description}>Aluno(a) de Engenharia de computação</p>
        </div>
        <a href={linkedin} target="_blank" rel="noopener noreferrer"></a>
    </div>
);

