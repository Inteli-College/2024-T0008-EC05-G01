import React from "react";
import styles from "../css/profile.module.css";

export const Membro = ({nome, imagem, linkedin}) => (
    <div className= {styles.profile_container} >
        <img src={imagem} alt={nome} />
        <p>{nome}</p>
        <a href={linkedin} target="_blank" rel="noopener noreferrer"></a>
    </div>
);

