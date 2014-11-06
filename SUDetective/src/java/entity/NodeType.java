/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "NODE_TYPE")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "NodeType.findAll", query = "SELECT n FROM NodeType n"),
    @NamedQuery(name = "NodeType.findByIdNODETYPE", query = "SELECT n FROM NodeType n WHERE n.idNODETYPE = :idNODETYPE"),
    @NamedQuery(name = "NodeType.findByName", query = "SELECT n FROM NodeType n WHERE n.name = :name")})
public class NodeType implements Serializable {
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idNODE_TYPE")
    private Integer idNODETYPE;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NAME")
    private String name;
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "nODETYPEidNODETYPE")
    private List<SuLog> suLogList;

    public NodeType() {
    }

    public NodeType(Integer idNODETYPE) {
        this.idNODETYPE = idNODETYPE;
    }

    public NodeType(Integer idNODETYPE, String name) {
        this.idNODETYPE = idNODETYPE;
        this.name = name;
    }

    public Integer getIdNODETYPE() {
        return idNODETYPE;
    }

    public void setIdNODETYPE(Integer idNODETYPE) {
        this.idNODETYPE = idNODETYPE;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @XmlTransient
    public List<SuLog> getSuLogList() {
        return suLogList;
    }

    public void setSuLogList(List<SuLog> suLogList) {
        this.suLogList = suLogList;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idNODETYPE != null ? idNODETYPE.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof NodeType)) {
            return false;
        }
        NodeType other = (NodeType) object;
        if ((this.idNODETYPE == null && other.idNODETYPE != null) || (this.idNODETYPE != null && !this.idNODETYPE.equals(other.idNODETYPE))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.NodeType[ idNODETYPE=" + idNODETYPE + " ]";
    }
    
}
